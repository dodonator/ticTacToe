import random
import os

# TicTacToe

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

def KI1_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	result = field
	running = True
	#print "It is the turn of the computer1."
	while running == True:
		row = random.randint(0,2)
		column = random.randint(0,2)
		if field[row][column] == ' ':
			result[row][column] = 'X'
			running = False
		else:
			pass
	return result

def KI2_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field

	result = field
	#print "It is the turn of the computer2."
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
			pass
			print 'This place is occupied!'
	return result

def Winner(field):

	winner = ''

	for row in field:
		if row == ['X','X','X']:
			winner = 'Computer1'
			return winner
		elif row == ['O','O','O']:
			winner = 'Computer2'
			return winner
		else:
			winner = ''
	
	columns = [[],[],[]]
	for row in field:
		columns[0].append(row[0])
		columns[1].append(row[1])
		columns[2].append(row[2])
	
	for col in columns:
		if col == ['X','X','X']:
			winner = 'Computer1'
			return winner
		elif col == ['O','O','O']:
			winner = 'Computer2'
			return winner
		else:
			winner = ''

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if dia1 == ['X','X','X'] or dia2 == ['X','X','X']:
		winner = 'Computer1'
		return winner
	elif dia1 == ['O','O','O'] or dia2 == ['O','O','O']:
		winner = 'Computer2'
		return winner
	else:
		winner = ''

	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return "Nobody"

	return winner

# Time to play!

computer1Score = 0
computer2Score = 0
com1Wins = 0
com2Wins = 0
counter = 0
number = 1000

while counter != number:
	#print counter
	#print 'Computer1: ' + str(computer1Score) + ' X'
	#print 'Computer2: ' + str(computer2Score) + ' O'
	#x = raw_input('Press Enter to continue!')
	os.system('clear')
	
	field = createNewField()
	win = Winner(field)
	turn = 0
	#printField(field)
	while win == '':
		if win == 'Nobody':
			print 'There is no winner.'
			break
		
		turn += 1
		#print 'Turn: ' + str(turn)
		field = KI1_Turn(field)
		#printField(field)
		win = Winner(field)
		if win == 'Computer1':
			break
		#os.system('clear')
		
		turn += 1
		#print 'Turn: ' + str(turn)
		field = KI2_Turn(field)
		#printField(field)		
		win = Winner(field)
		if win == 'Computer1':
			break
		#os.system('clear')
	
	#print 'The winner is: ' + win
	if win == 'Computer1':
		computer1Score += (10-turn)
		com1Wins += 1
	elif win == 'Computer2':
		computer2Score += (10-turn)
		com2Wins += 1
	counter += 1
maxScore = number * 4
print ''
print "Computer1 wins: " + str(com1Wins)
print "Computer1 win percent: " + str(float(float(com1Wins)/float(number)*100))
print "Computer1 score: " + str(computer1Score)
print "Computer1 score percent: " + str(float(float(computer1Score)/float(maxScore)*100))
print ''
print "Computer2 wins: " + str(com2Wins)
print "Computer2 win percent: " + str(float(float(com2Wins)/float(number)*100))
print "Computer2 score: " + str(computer2Score)
print "Computer2 score percent: " + str(float(float(computer2Score)/float(maxScore)*100))
print ''
