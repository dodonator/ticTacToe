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
	# print "It is the turn of the computer1."
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
	running = True
	# print "It is the turn of the computer2."
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
	# print "User it's your turn"
	while running == True:
		row = int(raw_input('Which row? '))
		column = int(raw_input('Which column? '))
		if field[row][column] == ' ':
			result[row][column] = 'X'
			running = False
		else:
			pass
			# print 'This place is occupied!'
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
counter = 0

while counter != 100000:
	print counter
	# print 'Computer1: ' + str(computer1Score)
	# print 'Computer2: ' + str(computer2Score)
	# x = raw_input('Press Enter to continue!')
	# os.system('clear')
	
	field = createNewField()
	win = Winner(field)
	turn = 0
	
	while win == '':
		if win == 'Nobody':
			# print 'There is no winner.'
			break
		
		turn += 1
		# print 'Turn: ' + str(turn)
		# printField(field)
		field = KI1_Turn(field)
		win = Winner(field)
		# os.system('clear')
		
		turn += 1
		# print 'Turn: ' + str(turn)
		# printField(field)
		field = KI2_Turn(field)
		win = Winner(field)
		# os.system('clear')
	
	# print 'The winner is: ' + win
	if win == 'Computer1':
		computer1Score += (10-turn)
	elif win == 'Computer2':
		computer2Score += (10-turn)
	counter += 1
print "Computer1: " + str(computer1Score)
print "Computer2: " + str(computer2Score)