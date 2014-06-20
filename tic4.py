import random
import os
import sys

# TicTacToe

player1Streak = []
player2Streak = []
player1Score = 0
player2Score = 0
player1Wins = 0
player2Wins = 0

def createNewField():
	result = []
	for i in range(3):
		tmp = []
		for i2 in range(3):
			tmp.append(' ')
		result.append(tmp)
	return result

def printField(field):
	print ''
	for element in field:
		print element
	print ''

def isFieldFull(field):
	occupiedPlaces = 0
	for row in field:
		for place in row:
			if place != ' ':
				occupiedPlaces += 1
			elif place == ' ':
				return False
	if occupiedPlaces == 9:
		return True

def danger(field,agressor):
	ownChar = ''
	if agressor == 'O':
		ownChar = 'X'
	elif agressor == 'X':
		ownChar = 'O'	
	result = field	
	for i in range(3):
		row = field[i]		
		agCounter = 0
		for place in row:
			if place == agressor:
				agCounter += 1
		if agCounter == 2:
			for i2 in range(3):
				if field[i][i2] == ' ':
					result[i][i2] = ownChar
					return result
	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	for i in range(3):
		col = columns[i]
		agCounter = 0
		for i2 in range(3):
			if col[i2] == agressor:
				agCounter += 1
		if agCounter == 2:
			for i2 in range(3):
				if field[i2][i] == ' ':
					result[i2][i] = ownChar
					return result
	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]
	agCounter = 0
	for i in range(3):
		if dia1[i] == agressor:
			agCounter += 1
	if agCounter == 2:
		if dia1[0] == ' ':
			result[0][0] = ownChar
			return result
		elif dia1[1] == ' ':
			result[1][1] = ownChar
			return result
		elif dia1[2] == ' ':
			result[2][2] = ownChar
			return result

	agCounter = 0
	for i in range(3):
		if dia2[i] == agressor:
			agCounter += 1
	if agCounter == 2:
		if dia2[0] == ' ':
			result[0][2] = ownChar
			return result
		elif dia2[1] == ' ':
			result[1][1] = ownChar
			return result
		elif dia2[2] == ' ':
			result[2][0] = ownChar
			return result
	
	return []

def victory(field,ownChar):
	result = field	
	for i in range(3):
		row = field[i]		
		charCounter = 0
		for place in row:
			if place == ownChar:
				charCounter += 1
		if charCounter == 2:
			for i2 in range(3):
				if field[i][i2] == ' ':
					result[i][i2] = ownChar
					return result
	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	for i in range(3):
		col = columns[i]
		charCounter = 0
		for i2 in range(3):
			if col[i2] == ownChar:
				charCounter += 1
		if charCounter == 2:
			for i2 in range(3):
				if field[i2][i] == ' ':
					result[i2][i] = ownChar
					return result
	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]
	charCounter = 0
	for i in range(3):
		if dia1[i] == ownChar:
			charCounter += 1
	if charCounter == 2:
		if dia1[0] == ' ':
			result[0][0] = ownChar
			return result
		elif dia1[1] == ' ':
			result[1][1] = ownChar
			return result
		elif dia1[2] == ' ':
			result[2][2] = ownChar
			return result

	charCounter = 0
	for i in range(3):
		if dia2[i] == ownChar:
			charCounter += 1
	if charCounter == 2:
		if dia2[0] == ' ':
			result[0][2] = ownChar
			return result
		elif dia2[1] == ' ':
			result[1][1] = ownChar
			return result
		elif dia2[2] == ' ':
			result[2][0] = ownChar
			return result
	return []

def randomAI(field,ownChar):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	result = field
	running = True
	print "It is the turn of the random AI"
	while running == True:
		row = random.randint(0,2)
		column = random.randint(0,2)
		if field[row][column] == ' ':
			result[row][column] = ownChar
			running = False
		else:
			pass
	return result

def easyAI(field,ownChar):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	if ownChar == 'X':
		enemyChar = 'O'
	elif ownChar == 'O':
		enemyChar = 'X'
	result = field
	print "It is the turn of the easy AI"
	for i in range(3):
		if ownChar in field[i] and enemyChar not in field[i]:
			if field[i][0] == ' ':
				result[i][0] = ownChar
				return result
			elif field[i][1] == ' ':
				field[i][1] = ownChar
				return result
			elif result[i][2] == ' ':
				result[i][2] = ownChar
				return result

	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for i in range(3):
		col = columns[i]
		if ownChar in col and enemyChar not in col:
			if field[0][i] == ' ':
				result[0][i] = ownChar
				return result
			elif field[1][i] == ' ':
				result[1][i] = ownChar
				return result
			elif field[2][i] == ' ':
				result[2][i] = ownChar
				return result

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if ownChar in dia1 and enemyChar not in dia1:
		if dia1[0] == ' ':
			result[0][0] = ownChar
			return result
		elif dia1[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia1[2] == ' ':
			result[2][2] = ownChar
			return result
	if ownChar in dia2 and enemyChar not in dia2:
		if dia2[0] == ' ':
			result[0][2] = ownChar
			return result
		elif dia2[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia2[2] == ' ':
			result[2][0] = ownChar
			return result

	row = random.randint(0,2)
	column = random.randint(0,2)
	result[row][column] = ownChar
	return result

def mediumAI(field,ownChar):
	# are there any empty places?
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	if ownChar == 'X':
		enemyChar = 'O'
	elif ownChar == 'O':
		enemyChar = 'X'
	result = field
	print "It is the turn of the medium AI"
	
	# Am I at risk?

	dan = danger(field,enemyChar)
	if dan == []:
		pass
	else:
		return dan

	# In which row or column are no enemy figures?

	for i in range(3):
		if ownChar in field[i] and enemyChar not in field[i]:
			if field[i][0] == ' ':
				result[i][0] = ownChar
				return result
			elif field[i][1] == ' ':
				field[i][1] = ownChar
				return result
			elif result[i][2] == ' ':
				result[i][2] = ownChar
				return result

	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for i in range(3):
		col = columns[i]
		if ownChar in col and enemyChar not in col:
			if field[0][i] == ' ':
				result[0][i] = ownChar
				return result
			elif field[1][i] == ' ':
				result[1][i] = ownChar
				return result
			elif field[2][i] == ownChar:
				result[2][i] = ownChar
				return result

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if ownChar in dia1 and enemyChar not in dia1:
		if dia1[0] == ' ':
			result[0][0] = ownChar
			return result
		elif dia1[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia1[2] == ' ':
			result[2][2] = ownChar
			return result

	if ownChar in dia2 and enemyChar not in dia2:
		if dia2[0] == ' ':
			result[0][2] = ownChar
			return result
		elif dia2[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia2[2] == ' ':
			result[2][0] = ownChar
			return result

	row = random.randint(0,2)
	column = random.randint(0,2)
	result[row][column] = ownChar

	return result

def heavyAI(field,ownChar):
	# are there any empty places?
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	if ownChar == 'X':
		enemyChar = 'O'
	elif ownChar == 'O':
		enemyChar = 'X'
	result = field
	print "It is the turn of the heavy AI"

	# Can i win?

	vic = victory(field,ownChar)
	if vic != []:
		return vic
	
	# Am I at risk?

	dan = danger(field,enemyChar)
	if dan == []:
		pass
	else:
		return dan

	# Which field has in itself?

	for i in range(3):
		if ownChar in field[i] and enemyChar not in field[i]:
			if field[i][0] == ' ':
				result[i][0] = ownChar
				return result
			elif field[i][1] == ' ':
				field[i][1] = ownChar
				return result
			elif result[i][2] == ' ':
				result[i][2] = ownChar
				return result

	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for i in range(3):
		col = columns[i]
		if ownChar in col and enemyChar not in col:
			if field[0][i] == ' ':
				result[0][i] = ownChar
				return result
			elif field[1][i] == ' ':
				result[1][i] = ownChar
				return result
			elif field[2][i] == ownChar:
				result[2][i] = ownChar
				return result

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if ownChar in dia1 and enemyChar not in dia1:
		if dia1[0] == ' ':
			result[0][0] = ownChar
			return result
		elif dia1[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia1[2] == ' ':
			result[2][2] = ownChar
			return result

	if ownChar in dia2 and enemyChar not in dia2:
		if dia2[0] == ' ':
			result[0][2] = ownChar
			return result
		elif dia2[1] == ' ':
			field[1][1] = ownChar
			return result
		elif dia2[2] == ' ':
			result[2][0] = ownChar
			return result

	row = random.randint(0,2)
	column = random.randint(0,2)
	result[row][column] = ownChar

	return result

def user(field,ownChar):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field

	result = field
	running = True
	print "User it's your turn"

	while running == True:
		row = raw_input('Which row? ')
		if len(row) == 2:
			tmp = row			
			row = int(tmp[0])
			column = int(tmp[1])
		else:		
			column = int(raw_input('Which column? '))
			row = int(row)
		if field[row][column] == ' ':
			result[row][column] = ownChar
			running = False
		else:
			print 'This place is occupied!'

	return result

def Winner(field):

	winner = ''

	for row in field:
		if row == player1Streak:
			winner = player1Name
			return winner
		elif row == player2Streak:
			winner = player2Name
			return winner
		else:
			winner = ''
	
	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for col in columns:
		if col == player1Streak:
			winner = player1Name
			return winner
		elif col == player2Streak:
			winner = player2Name
			return winner
		else:
			winner = ''

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if dia1 == player1Streak or dia2 == player1Streak:
		winner = player1Name
		return winner
	elif dia1 == player2Streak or dia2 == player2Streak:
		winner = player1Name
		return winner
	else:
		winner = ''

	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return "Nobody"

	return winner

# Preparation

os.system('clear')
player1Name = raw_input('Please enter your name: \n')
if len(player1Name) == 0:
	raise Exception('Error 504: Empty Name')
player2Name = 'AI'

player1Char = raw_input('Which char do you want to play (X/O)? ')
if player1Char == 'X':
	player2Char = 'O'
elif player1Char == 'O':
	player2Char = 'X'
else:
	raise Exception('Error 513: Wrong Char')

firstPlayer = user
firstPlayerChar = player1Char
secondPlayerChar = player2Char


os.system('clear')
print '0 : random KI'
print '1 : easy KI'
print '2 : medium KI'
print '3 : heavy KI'
print 'i : information about the KIs'
print 'q : quit' 
enemy = raw_input('Choose your enemy: ')
if enemy == 'q' or enemy == 'Q':
	sys.exit()
elif enemy == 'i' or enemy == 'I':
	file1 = open('infoBots.txt','r')
	content = file1.read()
	file1.close()
	os.system('clear')
	print content
	sys.exit()
elif enemy == '0':
	secondPlayer = randomAI
elif enemy == '1':
	secondPlayer = easyAI
elif enemy == '2':
	secondPlayer = mediumAI
elif enemy == '3':
	secondPlayer = heavyAI
else:
	raise Exception('Wrong input')
os.system('clear')
yn = raw_input('Do you want to start? (Y/N): ')
if yn == 'Y':
	firstPlayer = user
elif yn == 'N':
	tmp = firstPlayer
	tmp2 = firstPlayerChar
	firstPlayer = secondPlayer
	firstPlayerChar = secondPlayerChar
	secondPlayer = tmp
	secondPlayerChar = tmp2
os.system('clear')
for i in range(3):
	player1Streak.append(player1Char)
	player2Streak.append(player2Char)

roundNumber = 1

# Time to play!


answer = ''
while answer != 'q' and answer != 'Q':
	print 'Press q to exit or anything else to continue:'
	answer = raw_input(': ')
	if answer == 'q':
		break
	os.system('clear')	
	print 'Round: ' + str(roundNumber)
	print player1Name + ' Wins: ' + str(player1Wins)
	print player1Name + ' Score: ' + str(player1Score)
	print ''
	print player2Name + ' Wins: ' + str(player2Wins)
	print player2Name + ' Score: ' + str(player2Score)
	print ''
	print 30*'#'

	
	field = createNewField()
	win = Winner(field)
	turn = 0
	
	while win == '':
		if win == 'Nobody':
			print 'There is no winner.'
			break
		turn += 1
		print 'Round: ' + str(roundNumber)		
		print 'Turn: ' + str(turn)
		printField(field)
		firstPlayer(field,firstPlayerChar)
		print 30*'#'
		win = Winner(field)
		if win != '':
			printField(field)
			break
		turn += 1
		print 'Round: ' + str(roundNumber)
		print 'Turn: ' + str(turn)
		printField(field)
		secondPlayer(field,secondPlayerChar)		
		print 30*'#'
		win = Winner(field)
		if win != '':
			printField(field)
			break
	print 'The winner is: ' + str(win)	
	print 30*'#'
	if win == player1Name:
		player1Wins += 1
		player1Score += 10-turn
	elif win == player2Name:
		player2Wins += 1
		player2Score += 10-turn
	# Now change the starter!	
	tmp = firstPlayer
	tmp2 = firstPlayerChar
	firstPlayer = secondPlayer
	firstPlayerChar = secondPlayerChar
	secondPlayer = tmp
	secondPlayerChar = tmp2

	roundNumber += 1

