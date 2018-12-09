from tkinter import *


def isInsideBoard(b, lenA):
    row, col = b
    if (row > lenA - 1 or row < 0 or col > lenA - 1 or col < 0):
        return False
    return True

def printBoard(data):
    for c in data.board:
        print(c, "\n")

def findFlips(data,row,col,player):
    lenA = len(data.board)
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

def newGame(data):
    board = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "b", "w", "", "", ""],
        ["", "", "", "w", "b", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
    ]
    #print(data)
    init(data)

def init(data):
    data.rows = 8
    data.cols = 8
    data.margin = 5 # margin around grid
    data.player = "b"
    data.message = "Othello"
    data.winner = ""
    data.bscore = 2
    data.wscore = 2
    data.board = [
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "b", "w", "", "", ""],
    ["", "", "", "w", "b", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ]

def pointInGrid(x, y, data):
    # return True if (x, y) is inside the grid defined by data.
    return ((data.margin <= x <= data.width-data.margin) and
            (data.margin <= y <= data.height-data.margin))

def getCell(x, y, data):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(x, y, data)):
        return (-1, -1)
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    cellWidth  = gridWidth / data.cols
    cellHeight = gridHeight / data.rows
    row = (y - data.margin) // cellHeight
    col = (x - data.margin) // cellWidth
    # triple-check that we are in bounds
    row = min(data.rows-1, max(0, row))
    col = min(data.cols-1, max(0, col))
    return (row, col)

def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    columnWidth = gridWidth / data.cols
    rowHeight = gridHeight / data.rows
    x0 = data.margin + col * columnWidth
    x1 = data.margin + (col+1) * columnWidth
    y0 = data.margin + row * rowHeight
    y1 = data.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

def mousePressed(event, data):
    if event.x > 795 and event.y > 696:
        newGame(data)

    (row, col) = getCell(event.x, event.y, data)
    # select this (row, col) unless it is selected
    irow = int(row)
    icol = int(col)
    if(irow < 0 or icol < 0 or irow > 7 or icol > 7):
        return
    opponent = "b"
    if(data.player == "b"):
        opponent = "w"
    result = makeOthelloMove(data, irow, icol, data.player)
    if(result != 0):
        data.player = opponent
        data.message = "Othello"
        data.bscore, data.wscore = currentScore(data)
    else:
        if(canPlayerMove(data, data.player) == False):
            if(canPlayerMove(data, opponent) == False):
                data.message = "Game Over"
                data.winner = findWinner(data)
            else:
                data.message = "Opponents Turn"
                data.player = opponent
        else:
            data.message = "Invalid"

def keyPressed(event, data):
    pass

def redrawAll(canvas, data):

    # draw grid of cells
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            canvas.create_rectangle(x0, y0, x1, y1, fill = "grey")
            if(data.board[row][col] == "b"):
                canvas.create_oval((x0, y0), (x1, y1), fill="black")
            elif(data.board[row][col] == "w"):
                canvas.create_oval((x0, y0), (x1, y1), fill="white")

    canvas.create_text(data.width+data.width/8+50, data.height/8 - 45, text="SCORE:",
                       font="Arial 32 bold", fill="Red")

    canvas.create_oval((data.width+data.width/8, data.height/8), (data.width+data.width/4, data.height/4), fill="black")
    canvas.create_text(data.width+data.width/8+50, data.height/8+50, text=str(data.bscore),
                       font="Arial 36 bold", fill="White")
    canvas.create_oval((data.width+data.width/8, data.height/4), (data.width+data.width/4, data.height/2.667), fill="white")
    canvas.create_text(data.width+data.width/8+50, data.height/4+50, text=str(data.wscore),
                       font="Arial 36 bold", fill="Black")
    txt = "BLACK TURN"
    if (data.player == "w"):
        txt = "WHITE TURN"
    if(data.message == "Game Over"):
        txt = data.winner
    canvas.create_text(data.width+150, data.height - 145, text=data.message,
                       font="Arial 36 bold", fill="Red")
    canvas.create_text(data.width+150, data.height - 180, text=txt,
                       font="Arial 16 bold", fill="Red")
    canvas.create_rectangle(795, 696, 1100, 795, fill = "Silver")
    canvas.create_text(data.width+150, data.height - 55, text="New Game",
                       font="Arial 24 bold", fill="Red")

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width+300, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(800, 800)












