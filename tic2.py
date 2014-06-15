import random
import os
import sys

# TicTacToe

player1Name = "User"
player2Name = "KI"
player1Char = 'X'
player2Char = 'O'
player1Streak = []
player2Streak = []
player1Score = 0
player2Score = 0

print '0 : random KI'
print '1 : easy KI'
print '2 : medium KI'
print 'q : quit' 
enemy = raw_input('Choose your enemy: ')
if enemy == 'q' or enemy == 'Q':
	sys.exit()

for i in range(3):
	player1Streak.append(player1Char)
	player2Streak.append(player2Char)

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
	return []

def KI1_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	result = field
	running = True
	print "It is the turn of the random"
	while running == True:
		row = random.randint(0,2)
		column = random.randint(0,2)
		if field[row][column] == ' ':
			result[row][column] = 'O'
			running = False
		else:
			pass
	return result

def KI2_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field

	result = field
	print "It is the turn of the AI."
	for i in range(3):
		if 'O' in field[i] and 'X' not in field[i]:
			if field[i][0] == ' ':
				result[i][0] = 'O'
				return result
			elif field[i][1] == ' ':
				field[i][1] = 'O'
				return result
			elif result[i][2] == ' ':
				result[i][2] = 'O'
				return result

	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for i in range(3):
		col = columns[i]
		if 'O' in col and 'X' not in col:
			if field[0][i] == ' ':
				result[0][i] = 'O'
				return result
			elif field[1][i] == ' ':
				result[1][i] = 'O'
				return result
			elif field[2][i] == 'O':
				result[2][i] = 'O'
				return result

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if 'O' in dia1 and 'X' not in dia1:
		if dia1[0] == ' ':
			result[0][0] = 'O'
			return result
		elif dia1[1] == ' ':
			field[1][1] = 'O'
			return result
		elif dia1[2] == ' ':
			result[2][2] = 'O'
			return result
	if 'O' in dia2 and 'X' not in dia2:
		if dia2[0] == ' ':
			result[0][2] = 'O'
			return result
		elif dia2[1] == ' ':
			field[1][1] = 'O'
			return result
		elif dia2[2] == ' ':
			result[2][0] = 'O'
			return result

	row = random.randint(0,2)
	column = random.randint(0,2)
	result[row][column] = 'O'
	return result

def KI3_Turn(field):
	# are there any empty places?
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field

	result = field
	print "It is the turn of the AI2.0."
	
	# Am I at risk?

	dan = danger(field,'X')
	if dan == []:
		pass
	else:
		return dan

	# Which field has in itself?

	for i in range(3):
		if 'O' in field[i] and 'X' not in field[i]:
			if field[i][0] == ' ':
				result[i][0] = 'O'
				return result
			elif field[i][1] == ' ':
				field[i][1] = 'O'
				return result
			elif result[i][2] == ' ':
				result[i][2] = 'O'
				return result

	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for i in range(3):
		col = columns[i]
		if 'O' in col and 'X' not in col:
			if field[0][i] == ' ':
				result[0][i] = 'O'
				return result
			elif field[1][i] == ' ':
				result[1][i] = 'O'
				return result
			elif field[2][i] == 'O':
				result[2][i] = 'O'
				return result

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if 'O' in dia1 and 'X' not in dia1:
		if dia1[0] == ' ':
			result[0][0] = 'O'
			return result
		elif dia1[1] == ' ':
			field[1][1] = 'O'
			return result
		elif dia1[2] == ' ':
			result[2][2] = 'O'
			return result
	if 'O' in dia2 and 'X' not in dia2:
		if dia2[0] == ' ':
			result[0][2] = 'O'
			return result
		elif dia2[1] == ' ':
			field[1][1] = 'O'
			return result
		elif dia2[2] == ' ':
			result[2][0] = 'O'
			return result

	row = random.randint(0,2)
	column = random.randint(0,2)
	result[row][column] = 'O'
	return result

def USER_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	result = field
	running = True
	print "User it's your turn"
	while running == True:
		row = int(raw_input('Which row? '))
		column = int(raw_input('Which column? '))
		if field[row][column] == ' ':
			result[row][column] = 'X'
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

# Time to play!


answer = ''

while answer != 'q':
	print player1Name + ': ' + str(player1Score)
	print player2Name + ': ' + str(player2Score)
	print 'Press q to exit or anything else to continue'
	answer = raw_input(': ')
	if answer == 'q':
		break
	os.system('clear')
	
	field = createNewField()
	win = Winner(field)
	turn = 0
	
	while win == '':
		if win == 'Nobody':
			print 'There is no winner.'
			break
		
		turn += 1
		print 'Turn: ' + str(turn)
		printField(field)
		field = USER_Turn(field)
		win = Winner(field)
		if win == player1Name:
			break
		os.system('clear')
		
		turn += 1
		print 'Turn: ' + str(turn)
		printField(field)
		if enemy == '0':
			field = KI1_Turn(field)
		elif enemy == '1':
			field = KI2_Turn(field)
		elif enemy == '2':
			field = KI3_Turn(field)
		win = Winner(field)
		if win == player2Name:
			break
		os.system('clear')
	
	printField(field)
	print 'The winner is: ' + win
	if win == player1Name:
		player1Score += (10-turn)
	elif win == player2Name:
		player2Score += (10-turn)
print player1Name + ': ' + str(player1Score)
print player2Name + ': ' + str(player2Score)

