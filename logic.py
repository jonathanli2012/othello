def isInsideBoard(b, lenA):
    row, col = b

    if (row > lenA - 1 or row < 0 or col > lenA - 1 or col < 0):
        return False
    else:
        return True

def printBoard(data):
    for c in data.board:
        print(c, "\n")

def findFlips(data,row,col,player):
    lenA = len(data.board)

    #Determines opponent
    opponent = "b"
    if (player == "b"):
        opponent= "w"

    # 0=NW 1=N 2=NE 3=E 4=SE 5=S 6=SW 7=W
    positions = [(row+1,col+1,4),(row+1,col-1,6),(row-1,col+1,2),(row-1,col-1,0),(row-1,col,1),(row+1,col,5),(row,col+1,3),(row,col-1,7)]
    possiblePositions = []

    for c in positions:
        x,y,z=c
        if(isInsideBoard((x,y),lenA) and data.board[x][y] == opponent):
            possiblePositions.append(c)

    allList = []
    for c in possiblePositions:
        x,y,z = c
        flipList = []
        if(z == 0):
            for n in range(1, lenA):
                if (isInsideBoard((row - n, col - n), lenA) == True):
                    if(data.board[row - n][col - n] == opponent):
                        flipList.append((row - n, col - n))
                    elif(data.board[row - n][col - n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 1):
            for n in range(1, lenA):
                if (isInsideBoard((row - n, col), lenA) == True):
                    if (data.board[row - n][col] == opponent):
                        flipList.append((row - n, col))
                    elif(data.board[row - n][col] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 2):
            for n in range(1, lenA):
                if (isInsideBoard((row - n, col + n), lenA) == True):
                    if(data.board[row - n][col + n] == opponent):
                        flipList.append((row - n, col + n))
                    elif(data.board[row - n][col + n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 3):
            for n in range(1, lenA):
                if (isInsideBoard((row, col + n), lenA) == True):
                    if(data.board[row][col + n] == opponent):
                        flipList.append((row, col + n))
                    elif(data.board[row][col + n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 4):
            for n in range(1, lenA):
                if (isInsideBoard((row + n, col + n), lenA) == True):
                    if(data.board[row + n][col + n] == opponent):
                        flipList.append((row + n, col + n))
                    elif(data.board[row + n][col + n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 5):
            for n in range(1, lenA):
                if (isInsideBoard((row + n, col), lenA) == True):
                    if(data.board[row + n][col] == opponent):
                        flipList.append((row + n, col))
                    elif(data.board[row + n][col] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        elif (z == 6):
            for n in range(1, lenA):
                if (isInsideBoard((row + n, col - n), lenA) == True):
                    if(data.board[row + n][col - n] == opponent):
                        flipList.append((row + n, col - n))
                    elif(data.board[row + n][col - n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break
        else:
            for n in range(1, lenA):
                if (isInsideBoard((row, col - n), lenA) == True):
                    if(data.board[row][col - n] == opponent):
                        flipList.append((row, col - n))
                    elif(data.board[row][col - n] == ""):
                        break
                    else:
                        allList.append(flipList)
                        break
                else:
                    break

    return allList

def makeOthelloMove(data, row, col, player):
    lenA = len(data.board)
    if(isInsideBoard((row,col), lenA) == False or data.board[row][col] != ""):
        return 0
    flips = findFlips(data,row,col,player)
    if(len(flips) <= 0):
        return 0
    else:
        piecesFlipped = 0
        data.board[row][col] = player
        for c in flips:
            for d in c:
                x,y = d
                data.board[x][y] = player
                piecesFlipped += 1
    return piecesFlipped

def canPlayerMove(data, player):
    lenA = len(data.board)
    for i in range (lenA):
        for j in range(lenA):
            if(data.board[i][j] == ""):
                flipped = findFlips(data,i,j,player)
                if(len(flipped) != 0):
                    return True
    return False

def findWinner(data):
    #Called when board is filled
    lenA = len(data.board)
    bCount, wCount = 0, 0
    for i in range (lenA):
        bCount += data.board[i].count("b")
        wCount += data.board[i].count("w")
    if(bCount > wCount): return "BLACK WINS"
    elif(bCount < wCount): return "WHITE WINS"
    return "TIE GAME"

def currentScore(data):
    lenA = len(data.board)
    bCount, wCount = 0, 0
    for i in range (lenA):
        bCount += data.board[i].count("b")
        wCount += data.board[i].count("w")
    return (bCount,wCount)