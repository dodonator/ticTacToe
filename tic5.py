# Warning: Just in developing
# Theoretical this version supports all sizes of fields
# with the condition that size%2 = 1
import random
import os
import copy

# TODO:
# game-function to play the Round() function
# more cheater
# invincible AI
# nicer output
# nicer input
# fix the semantic bugs!!!


def call_log(f):

    def aux(*args, **kwargs):
        print("called {} with {}, {}".format(f.__name__, args, kwargs))
        retval = f(*args, **kwargs)
        p = ("returned {} (input values are {}, {})")
        print p.format(retval, args, kwargs)
        return retval

    return aux


def dbg(toPrint):
    print repr(toPrint)
    return


def setPlayer(function):
    result = []
    playerFunction = function
    playerName = raw_input('Please input the name of the player: ')
    playerChar = raw_input('Please input the char of the player: ')
    result = [playerFunction, playerName, playerChar, 0]
    return result


def createNewField(size):
    result = []
    for i in range(size):
        tmp = []
        for i2 in range(size):
            tmp.append(' ')
        result.append(tmp)
    return result


def printField_old(field):
    print ''
    for element in field:
        print element
    print ''


def printField(field):
    print('')
    line = '{} | {} | {}'
    sepa = '---------'
    print(line.format(*field[0]))
    print(sepa)
    print(line.format(*field[1]))
    print(sepa)
    print(line.format(*field[2]))
    print('')


def printField2(field, size):
    result = []
    k = 0
    for i in range(size):
        result.append([])
    for i in range(size):
        for i2 in range(size):
            if field[i][i2] == ' ':
                result[i].append(str(k+i2))
            else:
                result[i].append(field[i][i2])
        k += size
    for element in result:
        print element


def printFieldM(field):
    size = len(field)
    man = []
    for r in range(size):
        man.append([])
    for r in range(size):
        for c in range(size):
            man[r].append(str(str(r)+'|'+str(c)))
    for i in range(size):
        print str(field[i]) + '    ' + str(man[i])


def getDIA(field, size):
    dia1 = []
    dia2 = []
    for i in range(size):
        dia1.append(field[i][i])
        dia2.append(field[i][size-(i+1)])
    result = [dia1, dia2]
    return result


def getCOL(field, size):
    columns = []
    for i in range(size):
        columns.append([])
    for row in field:
        for i in range(size):
            columns[i].append(row[i])
    return columns


def getFieldStatus(field, size):
    occupiedPlaces = 0
    for row in field:
        for place in row:
            if place != ' ':
                occupiedPlaces += 1
            elif place == ' ':
                pass
    return occupiedPlaces


def danger(field, size, ownChar):
    if ownChar == 'O':
        agressor = 'X'
    elif ownChar == 'X':
        agressor = 'O'
    result = field
    for i in range(size):
        row = field[i]
        agCounter = 0
        for place in row:
            if place == agressor:
                agCounter += 1
        if agCounter == (size-1):
            for i2 in range(size):
                if field[i][i2] == ' ':
                    result[i][i2] = ownChar
                    return result
    columns = getCOL(field, size)
    for i in range(size):
        col = columns[i]
        agCounter = 0
        for i2 in range(size):
            if col[i2] == agressor:
                agCounter += 1
        if agCounter == (size-1):
            for i2 in range(size):
                if field[i2][i] == ' ':
                    result[i2][i] = ownChar
                    return result
    dia1 = getDIA(field, size)[0]
    dia2 = getDIA(field, size)[1]
    agCounter = 0
    for i in range(size):
        if dia1[i] == agressor:
            agCounter += 1
    if agCounter == (size-1):
        for i in range(size):
            if dia1[i] == ' ':
                result[i][i] = ownChar
                return result
    agCounter = 0
    for i in range(size):
        if dia2[i] == agressor:
            agCounter += 1
    if agCounter == (size-1):
        for i2 in range(size):
            if dia2[i] == ' ':
                result[i][size-(i+1)] = ownChar
                return result
    return []


def victory(field, size, ownChar):
    fullLine = []
    for i in range(size):
        fullLine.append(ownChar)

    result = field

    charCounter = 0
    for i in range(size):
        for i2 in range(size):
            if field[i][i2] == ownChar:
                charCounter += 1
        if charCounter == (size-1):
            for i3 in range(size):
                if field[i][i3] == ' ':
                    result[i][i3] = ownChar
                    return result

    charCounter = 0
    columns = getCOL(field, size)
    for i in range(size):
        for i2 in range(size):
            if columns[i][i2] == ownChar:
                charCounter += 1
        if charCounter == (size-1):
            for i3 in range(size):
                if columns[i][i3] == ' ':
                    columns[i][i3] = ownChar
                    result = getCOL(columns, size)
                    return result

    dia1 = getDIA(field, size)[0]
    dia2 = getDIA(field, size)[1]
    charCounter = 0
    for i in range(size):
        if dia1[i] == ownChar:
            charCounter += 1
    if charCounter == (size-1):
        for i in range(size):
            if dia1[i] == ' ':
                result[i][i] = ownChar
                return result
    charCounter = 0
    for i in range(size):
        if dia2[i] == ownChar:
            charCounter += 1
    if charCounter == (size-1):
        for i in range(size):
            if dia2[i] == ' ':
                result[i][size-(i+1)] = ownChar
                return result
    return []


def Winner(field, size, player1Char, player2Char):
    winner = ' '
    player1Streak = []
    player2Streak = []
    for i in range(size):
        player1Streak.append(player1Char)
        player2Streak.append(player2Char)

    for row in field:
        if row == player1Streak:
            winner = player1Char
            return winner
        elif row == player2Streak:
            winner = player2Char
            return winner
        else:
            winner = ' '

    columns = getCOL(field, size)

    for col in columns:
        if col == player1Streak:
            winner = player1Char
            return winner
        elif col == player2Streak:
            winner = player2Char
            return winner
        else:
            winner = ' '
    dia1 = getDIA(field, size)[0]
    dia2 = getDIA(field, size)[1]

    if dia1 == player1Streak or dia2 == player1Streak:
        winner = player1Char
        return winner
    elif dia1 == player2Streak or dia2 == player2Streak:
        winner = player1Char
        return winner
    else:
        winner = ' '

    fieldStatus = getFieldStatus(field, size)
    if fieldStatus == 9:
        return "Nobody"

    return winner


@call_log
def AI_phase0(field, size, ownChar):
    result = field
    if ownChar == 'X':
        enemyChar = 'O'
    elif ownChar == 'O':
        enemyChar = 'X'

    if getFieldStatus(field, size) == 0:
        result[int(size/2)][int(size/2)] = ownChar
        return result
    elif getFieldStatus(field, size) == 1:
        if field[int(size/2)][int(size/2)] == enemyChar:
            r = random.randint(0, 3)
            if r == 0:
                result[0][0] = ownChar
            elif r == 1:
                result[0][size-1] = ownChar
            elif r == 2:
                result[size-1][0] = ownChar
            elif r == 3:
                result[size-1][size-1] = ownChar
            return result
    return []


@call_log
def AI_phase3(field, size, ownChar):
    if ownChar == 'X':
        enemyChar = 'O'
    elif ownChar == 'O':
        enemyChar = 'X'
    result = copy.deepcopy(field)
    for r in range(size):
        if ownChar in field[r] and enemyChar not in field[r]:
            for c in range(size):
                if field[r][c] == ' ':
                    result[r][c] = ownChar
                    return result
    columns = getCOL(field, size)
    for c in range(size):
        if ownChar in columns[c] and enemyChar not in columns[c]:
            for r in range(size):
                if field[r][c] == ' ':
                    result[r][c] = ownChar
                    return result
    dia1 = getDIA(field, size)[0]
    dia2 = getDIA(field, size)[1]
    if ownChar in dia1 and enemyChar not in dia1:
        for i in range(size):
            if dia1[i] == ' ':
                result[i][i] = ownChar
                return result
    elif ownChar in dia2 and enemyChar not in dia2:
        for i in range(size):
            if dia2[i] == ' ':
                result[i][size-(i+1)] = ownChar
                return result
    result = []
    return result


def AI(field, size, ownChar):
    # Phase 0
    result = AI_phase0(field, size, ownChar)
    if result != []:
        return result
    # Phase 1
    result = victory(field, size, ownChar)
    if result != []:
        return result
    # Phase 2
    result = danger(field, size, ownChar)
    if result != []:
        return result
    # Phase 3
    result = AI_phase3(field, size, ownChar)
    if result != []:
        return result
    # Phase 4
    result = field

    print("entering something")
    while True:
        r = random.randint(0, size-1)
        c = random.randint(0, size-1)
        if field[r][c] == ' ':
            result[r][c] = ownChar
            return result


def user(field, size, ownChar):
    result = field
    while True:
        printField(field)
        row = int(raw_input('Which row (0-'+str(size-1)+'): '))
        column = int(raw_input('Which column (0-'+str(size-1)+'): '))
        if field[row][column] == ' ':
            result[row][column] = ownChar
            return result
        else:
            os.system('clear')


# I hope you enjoy my cheat functions


def cheater_shuffle(field, size, ownChar):
    result = field
    if ownChar == 'X':
        enemyChar = 'O'
    elif ownChar == 'O':
        enemyChar = 'X'
    occupiedPlaces = 1  # Because of this 1 the function add one figure
    for r in range(size):
        for c in range(size):
            if field[r][c] != ' ':
                occupiedPlaces += 1
    for i in range(occupiedPlaces):
        r = random.randint(0, size-1)
        c = random.randint(0, size-1)
        result[r][c] = random.choice([ownChar, enemyChar])
    return result


def cheater_shuffle_na(field, size, ownChar):
    # na means that this function don't add a figure
    result = field
    if ownChar == 'X':
        enemyChar = 'O'
    elif ownChar == 'O':
        enemyChar = 'X'
    occupiedPlaces = 0
    for r in range(size):
        for c in range(size):
            if field[r][c] != ' ':
                occupiedPlaces += 1
    for i in range(occupiedPlaces):
        r = random.randint(0, size-1)
        c = random.randint(0, size-1)
        result[r][c] = random.choice([ownChar, enemyChar])
    return result


def cheater_invert_na(field, size, ownChar):
    # na means that this function don't add a figure
    result = field
    if ownChar == 'X':
        enemyChar = 'O'
    elif ownChar == 'O':
        enemyChar = 'X'
    for r in range(size):
        for c in range(size):
            if field[r][c] == ownChar:
                result[r][c] = enemyChar
            elif field[r][c] == enemyChar:
                result[r][c] = ownChar
    return result


def cheater_swap_na(field, size, ownChar):
    # na means that this function don't add a figure
    result = field
    r1 = random.randint(0, size-1)
    c1 = random.randint(0, size-1)
    r2 = random.randint(0, size-1)
    c2 = random.randint(0, size-1)
    result[r1][c1] = field[r2][c2]
    result[r2][c2] = field[r1][c1]
    return result


def cheater_AI(field, size, ownChar):
    result = field
    result = cheater_invert_na(result, size, ownChar)
    result = AI(result, size, ownChar)
    return result


# player = [function, name, char, score]

def Round(field, size, player1, player2):

    player1Function = player1[0]
    player2Function = player2[0]
    player1Char = player1[2]
    player2Char = player2[2]

    victor = Winner(field, size, player1Char, player2Char)
    if victor == ' ':
        pass
    else:
        if victor == 'Nobody':
            return 'Nobody'
        else:
            return victor

    field = player1Function(field, size, player1Char)
    printField(field)

    victor = Winner(field, size, player1Char, player2Char)
    if victor == ' ':
        pass
    else:
        if victor == 'Nobody':
            return 'Nobody'
        else:
            return victor

    field = player2Function(field, size, player2Char)
    printField(field)

    victor = Winner(field, size, player1Char, player2Char)
    if victor == ' ':
        pass
    else:
        if victor == 'Nobody':
            return 'Nobody'
        else:
            return victor

    print "returning field"
    return field


def Game(size, player1, player2):
    field = createNewField(size)
    result = []
    while result(isinstance) != isinstance(''):

        result = Round(field, size, player1, player2)
        # print repr(result)
        if result == 'Nobody':
            print 'Nobody wins'
            return [player1, player2]
        elif result == player1[2]:
            print str(player1[1]) + ' wins'
            player1[3] += 1
            return [player1, player2]
        elif result == player2[2]:
            print str(player2[1]) + ' wins'
            player2[3] += 1
            return [player1, player2]

        field = result

    if result == 'Nobody':
        print 'Nobody wins'
        return [player1, player2]
    elif result == player1[2]:
        print str(player1[1]) + ' wins'
        player1[3] += 1
        return [player1, player2]
    elif result == player2[2]:
        print str(player2[1]) + ' wins'
        player2[3] += 1
        return [player1, player2]

size = 3
function1 = user
function2 = AI

rounds = 100

player1 = setPlayer(function1)
player2 = setPlayer(function2)

result = [player1, player2]

counter = 0
while counter != rounds:
    result = Game(size, result[0], result[1])

player1 = result[0]
player2 = result[1]

print str(player1[1]) + ' score: ' + str(player1[3])
print str(player2[1]) + ' score: ' + str(player2[3])
