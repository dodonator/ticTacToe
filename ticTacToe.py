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


def KI_Turn(field):
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return field
	result = field
	running = True
	"It is the turn of the computer."
	while running == True:
		row = random.randint(0,2)
		column = random.randint(0,2)
		if field[row][column] == ' ':
			result[row][column] = 'O'
			running = False
		else:
			pass
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
		if row == ['X','X','X']:
			winner = 'User'
			return winner
		elif row == ['O','O','O']:
			winner = 'Computer'
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
			winner = 'User'
			return winner
		elif col == ['O','O','O']:
			winner = 'Computer'
			return winner
		else:
			winner = ''

	dia1 = [field[0][0],field[1][1],field[2][2]]
	dia2 = [field[0][2],field[1][1],field[2][0]]

	if dia1 == ['X','X','X'] or dia2 == ['X','X','X']:
		winner = 'User'
		return winner
	elif dia1 == ['O','O','O'] or dia2 == ['O','O','O']:
		winner = 'Computer'
		return winner
	else:
		winner = ''
	fieldStatus = isFieldFull(field)
	if fieldStatus == True:
		return "Nobody"
	return winner

# Time to play!

userScore = 0
computerScore = 0
answer = ''

while answer != 'q':
	print 'User: ' + str(userScore)
	print 'Computer: ' + str(computerScore)
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
		if win == 'User':
			break
		os.system('clear')
		
		turn += 1
		print 'Turn: ' + str(turn)
		printField(field)
		field = KI_Turn(field)
		win = Winner(field)
		if win == 'Computer':
			break
		os.system('clear')
	
	printField(field)
	print 'The winner is: ' + win
	if win == 'User':
		userScore += (10-turn)
	elif win == 'Computer':
		computerScore += (10-turn)

print "User: " + str(userScore)
print "Computer: " + str(computerScore)
