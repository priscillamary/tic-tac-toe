# Project X, due August 21, 2020
import csv
import pandas
from itertools import zip_longest
from PIL import Image
from playsound import playsound
import turtle
import time

s = turtle.Screen()
t = turtle.Turtle()

cellSize = 250
penStrokeGrid = 15
penStrokeX = 8
penFillGrid = 'black'
penFillX = 'green'
penFillOh = 'blue'
t.color(penFillGrid)
t.width(penStrokeGrid+5)
t.speed('fast')

length = cellSize/3
r = cellSize/4
numberFontSize = 15

gameBoard = ['-','-','-','-','-','-','-','-','-']

promptX = "X: Enter a number"
promptO = "O: Enter a number"

XWins = 'X won here!'
OWins = 'O won here!'
draw = "It's a draw here"

scoreX = 0
scoreO = 0

triplets = ((0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6))

vertRight = ((cellSize/3, (cellSize)), # begin point
                (cellSize/3, (-cellSize))) # end point
vertLeft = ((-cellSize/3, cellSize), # begin point
                (-cellSize/3, -cellSize)) # end point
horizTop = ((-cellSize, (cellSize/(3))), # begin point
                (cellSize, (cellSize/(3)))) # end point
horizBot = ((-cellSize, (-cellSize/3)), # begin point
                (cellSize, (-cellSize/3))) # end point

def drawLines(t, vertRight, vertLeft, horizTop, horizBot):
    t.up()
    t.goto(vertRight[0][0],vertRight[0][1])
    t.down()
    t.goto(vertRight[1][0],vertRight[1][1])

    t.up()
    t.goto((vertLeft[0][0]),(vertLeft[0][1]))
    t.down()
    t.goto(vertLeft[1][0],vertLeft[1][1])

    t.up()
    t.goto((horizTop[0][0]),(horizTop[0][1]))
    t.down()
    t.goto(horizTop[1][0],horizTop[1][1])
    
    t.up()
    t.goto((horizBot[0][0]),(horizBot[0][1]))
    t.down()
    t.goto(horizBot[1][0],horizBot[1][1])

CELL_CENTERS = ((-cellSize*(2/3), cellSize*(2/3))
                ,(0, cellSize*(2/3))
                ,(cellSize*(2/3), cellSize*(2/3))
                ,(-cellSize*(2/3), 0)
                ,(0, 0)
                ,(cellSize*(2/3), 0)
                ,(-cellSize*(2/3), -cellSize*(2/3))
                ,(0, -cellSize*(2/3))
                ,(cellSize*(2/3), -cellSize*(2/3)))

s.bgcolor('plum')
s.register_shape("ezgif.com-apng-to-gif.gif")
t.shape("ezgif.com-apng-to-gif.gif")
t.up()
t.goto(cellSize,-cellSize)
userName1 = s.textinput("X", "X: Hi! Enter a username")
userName2 = s.textinput("O", "O: Now, enter another username")
userName1 = str(userName1)
userName2 = str(userName2)

getNumSessions = s.numinput("value", "How many points for a player to win?")
while (getNumSessions == 0):
    getNumSessions = s.numinput("value", "Invalid input. Pick a number greater than zero")
    if (getNumSessions != 0):
        break  
getNumSessions = int(getNumSessions)

def drawGrid():
    t.shape("arrow")
    t.color('black')
    t.width(20)
    drawLines(t, vertRight, vertLeft, horizTop, horizBot)

def drawXAtMidpoint(t, length):
    t.down()
    t.forward(length)
    t.backward(length*2)
    t.forward(length)

def concentricCircle(t, r):
    t.speed('fast')
    t.circle(r)

def getToMidPointOh(player2Number):
    t.color(penFillOh)
    t.width(penStrokeX)
    
    t.up()

    midpoint = CELL_CENTERS[player2Number]
    
    t.goto(midpoint[0]+r*(2/3),midpoint[1]+r*(2/3))
    t.down()
    concentricCircle(t, r)
            
    t.up()
    t.goto(0,0)

def getToMidPointX(player1Number):
    t.color(penFillX)
    t.width(penStrokeX)

    t.up()
    
    midpoint = CELL_CENTERS[player1Number]
    
    t.goto(midpoint[0],midpoint[1])
    t.setheading(45)
    drawXAtMidpoint(t, length)
    t.up()
    t.setheading(135)
    drawXAtMidpoint(t, length)
    
    t.up()
    t.goto(0,0)

def drawCell(cell):
    t.color('black')
    t.up()
    
    midpoint = CELL_CENTERS[cell]
    
    t.goto(midpoint[0]-cellSize/30,midpoint[1]-cellSize/25)

    t.down()
    t.write(cell, font=("Open Sans",numberFontSize,"normal"))
    
    t.up()
    t.goto(0,0)

def drawX(player1Number):
    getToMidPointX(player1Number)

def drawOh(player2Number):
    getToMidPointOh(player2Number)

def writeCells():
    for printNumber in range(9):
        drawCell(printNumber)

def drawWins(gameBoard,player):
    if (gameBoard[0] == player
        and gameBoard[1] == player
        and gameBoard[2] == player):
        t.up()
        t.goto(-cellSize,(7/8)*cellSize)
        t.down()
        t.color('red')
        t.right(135)
        t.forward(2*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.up()
        return gameBoard
    elif (gameBoard[3] == player
        and gameBoard[4] == player
        and gameBoard[5] == player):
        t.up()
        t.goto(-cellSize,-cellSize/6)
        t.down()
        t.color('red')
        t.right(135)
        t.forward(2*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.left(90)
        t.forward(2*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.up()
        return gameBoard
    elif (gameBoard[6] == player
        and gameBoard[7] == player
        and gameBoard[8] == player):
        t.up()
        t.goto(-cellSize,-.85*cellSize)
        t.down()
        t.color('red')
        t.right(135)
        t.forward(2*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.left(90)
        t.forward(2*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.up()
        return gameBoard
    elif (gameBoard[0] == player
        and gameBoard[3] == player
        and gameBoard[6] == player):
        t.up()
        t.goto(-cellSize/2,-cellSize)
        t.down()
        t.color('red')
        t.left(45)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.up()
        return gameBoard
    elif (gameBoard[1] == player
        and gameBoard[4] == player
        and gameBoard[7] == player):
        t.up()
        t.goto(.15*cellSize,-cellSize)
        t.down()
        t.color('red')
        t.left(45)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.up()
        return gameBoard
    elif(gameBoard[2] == player
        and gameBoard[5] == player
        and gameBoard[8] == player):
        t.up()
        t.goto(.85*cellSize,-cellSize)
        t.down()
        t.color('red')
        t.left(45)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2*cellSize)
        t.up()
        return gameBoard
    elif(gameBoard[0] == player
        and gameBoard[4] == player
        and gameBoard[8] == player):
        t.up()
        t.goto(-.9*cellSize,0.7*cellSize)
        t.down()
        t.color('red')
        t.right(180)
        t.forward(2.3*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.left(90)
        t.forward(2.3*cellSize)
        t.left(90)
        t.forward(cellSize/3)
        t.up()
        return gameBoard
    elif(gameBoard[2] == player
        and gameBoard[4] == player
        and gameBoard[6] == player):
        t.up()
        t.goto(-0.95*cellSize,-.7*cellSize)
        t.down()
        t.color('red')
        t.left(270)
        t.forward(2.3*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.right(90)
        t.forward(2.3*cellSize)
        t.right(90)
        t.forward(cellSize/3)
        t.up()
        return gameBoard

def isDraw():
    s.bgcolor('black')
    t.up()
    t.down()
    t.up()
    t.color('red')
    t.goto(0,0)
    t.goto(-260,0)
    t.write('No winner this time!', font=('Open Sans',55,'bold'))
    return

def gameOver(t,s):
    s.bgcolor('black')
    s.bgpic("turtles_swim.gif")
    t.width(25)
    t.color('indigo')
    t.up()
    t.goto(-1.015*cellSize,cellSize-30)
    t.down()
    t.write("Game Over", font=("Open Sans", 100,"bold"))
    playsound("file:///Users/priscillamaryanski/Desktop/project-x-repo/game-over.mp3")
    t.up()
    t.goto(3*cellSize,3*cellSize)
    s.clear()
    
def showWinnerX(t,showOneWinner):
        t.up()
        t.color('blue')
        t.goto(-1.18*cellSize,cellSize)
        t.down()
        t.write(userName1 + " wins!", font=("Open Sans", 55,"bold"))
    
def showWinnerO(t,showOneWinner):
        t.up()
        t.color('blue')
        t.goto(-1.18*cellSize,cellSize)
        t.down()
        t.write(userName2 + " wins!", font=("Open Sans", 55,"bold"))

def isWin(t,triplets,gameBoard):
    for i in triplets:
        cell1 = i[0]
        cell2 = i[1]
        cell3 = i[2]
                
        a = gameBoard[cell1]
        b = gameBoard[cell2]
        c = gameBoard[cell3]
        
        a,b,c = gameBoard[i[0]],gameBoard[i[1]],gameBoard[i[2]]
        print(a,b,c)
        combo = [a,b,c]
        
        if (i in triplets
              and 'X' in gameBoard[0]
              and 'X' in gameBoard[1]
              and 'X' in gameBoard[2]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[3]
              and 'X' in gameBoard[4]
              and 'X' in gameBoard[5]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[6]
              and 'X' in gameBoard[7]
              and 'X' in gameBoard[8]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[0]
              and 'X' in gameBoard[4]
              and 'X' in gameBoard[8]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[2]
              and 'X' in gameBoard[4]
              and 'X' in gameBoard[6]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[0]
              and 'X' in gameBoard[3]
              and 'X' in gameBoard[6]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[1]
              and 'X' in gameBoard[4]
              and 'X' in gameBoard[7]):
            saveWin = 'P'
            return saveWin
        elif (i in triplets
              and 'X' in gameBoard[2]
              and 'X' in gameBoard[5]
              and 'X' in gameBoard[8]):
            saveWin = 'P'
            return saveWin
        
        if (i in triplets
              and 'O' in gameBoard[0]
              and 'O' in gameBoard[1]
              and 'O' in gameBoard[2]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[3]
              and 'O' in gameBoard[4]
              and 'O' in gameBoard[5]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[6]
              and 'O' in gameBoard[7]
              and 'O' in gameBoard[8]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[0]
              and 'O' in gameBoard[4]
              and 'O' in gameBoard[8]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[2]
              and 'O' in gameBoard[4]
              and 'O' in gameBoard[6]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[0]
              and 'O' in gameBoard[3]
              and 'O' in gameBoard[6]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[1]
              and 'O' in gameBoard[4]
              and 'O' in gameBoard[7]):
            saveWin = 'L'
            return saveWin
        elif (i in triplets
              and 'O' in gameBoard[2]
              and 'O' in gameBoard[5]
              and 'O' in gameBoard[8]):
            saveWin = 'L'
            return saveWin
        
        drawPossible = [['X','X','O'],['X','O','X'],
                        ['X','X','O'], ['X','O','X'],
                        [ 'O','O','X'],['O','X','O'],
                        ['X','O','O'], ['O','X','X']]
        
        if ('-' not in gameBoard
            and combo in drawPossible):
            saveWin = 'this is a draw'
            return saveWin

def initTurtle(XWins,promptX,promptO,gameBoard,playerNumber):
    player1Number = s.numinput("Enter a number",promptX,minval=0,maxval=8)
    player1Number = int(player1Number)
    if (player1Number != None):
        while (gameBoard[player1Number] != '-'):
            promptX = "X: Number taken. Try again"
            player1Number = s.numinput("Enter a number",promptX,minval=0,maxval=8)
            player1Number = int(player1Number)
            if (gameBoard[player1Number] == '-'):
                break
        player1Number = int(player1Number)
        gameBoard[player1Number] = 'X'
        drawX(player1Number)
        print(gameBoard)     
        saveWin = isWin(t,triplets,gameBoard)
        if (saveWin == 'P' and saveWin != 'L'):
            return saveWin
        elif (saveWin == 'this is a draw'):
            return saveWin
        
        player2Number = s.numinput("Enter a number",promptO,minval=0,maxval=8)
        player2Number = int(player2Number)
        if (player2Number != None):
            while (gameBoard[player2Number] != '-'):
                promptO = "O: Number taken. Try again"
                player2Number = s.numinput("Enter a number",promptO,minval=0,maxval=8)
                player2Number = int(player2Number)
                if (gameBoard[player2Number] == '-'):
                    break
            player2Number = int(player2Number)
            gameBoard[player2Number] = 'O'
            drawOh(player2Number)
            print(gameBoard)
            saveWin = isWin(t,triplets,gameBoard)
            if (saveWin == 'L' and saveWin != 'P'):
                return saveWin
            elif (saveWin == 'this is a draw'):
                return saveWin

def playTTT(t,s,gameBoard,XWins,OWins):
    for i in range(8):
        saveWin = initTurtle(XWins,promptX,promptO,gameBoard,i)
        if (saveWin == 'P'):
            s.bgcolor('black')
            gameOverOutput = print(XWins)
            t.up()
            t.down()
            playerX = 'X'
            drawWins(gameBoard,playerX)
            gameBoard = ['-','-','-','-','-','-','-','-','-']
            t.up()
            t.goto(-200,0)
            t.down()
            t.color('gold')
            t.write('X won here!', font=('Open Sans',70,'bold'))
            playsound('file:///Users/priscillamaryanski/Desktop/project-x-repo/Old%20victory%20sound%20roblox.mp3')
            session = 'Session complete! X won'
            return session
        elif (saveWin == 'L'):
            s.bgcolor('black')
            gameOverOutput = print(OWins)
            t.up()
            t.down()
            playerO = 'O'
            drawWins(gameBoard,playerO)
            gameBoard = ['-','-','-','-','-','-','-','-','-']
            t.up()
            t.goto(-200,0)
            t.down()
            t.color('gold')
            t.write('O won here!', font=('Open Sans',70,'bold'))
            playsound("file:///Users/priscillamaryanski/Desktop/project-x-repo/Old%20victory%20sound%20roblox.mp3")
            session = 'Session complete! O won'
            return session
        
        elif (saveWin == 'this is a draw'):
                isDraw()
                gameBoard = ['-','-','-','-','-','-','-','-','-']
                playsound("file:///Users/priscillamaryanski/Desktop/project-x-repo/The%20Price%20is%20Right%20Losing%20Horn%20-%20Gaming%20Sound%20Effect%20(HD).mp3")
                session = 'draw'
                return session
        
def continuePlay(t,s,scoreX,scoreO,gameBoard,promptX,promptO):
    s.bgcolor('gold')
    print(getNumSessions)
    if (getNumSessions > 1):
        numOfSessions = getNumSessions
    elif (getNumSessions == 1):
        numOfSessions = getNumSessions
    while (scoreX < numOfSessions or scoreO < numOfSessions):
        s.bgcolor('white')
        
        promptX = "X: Enter a number"
        promptO = "O: Enter a number"
        
        playsound("file:///Users/priscillamaryanski/Desktop/project-x-repo/1-up.mp3")
        drawGrid()
        t.up()
        t.goto(cellSize/3, cellSize)
        t.down()
        t.goto(cellSize/3, -cellSize)
        t.up()
        
        writeCells()
        t.color('black')
        t.up()
        t.goto(-1.1*cellSize,cellSize+30)
        t.down()
        t.write(userName1 + " (X):  " + str(scoreX), font=("Open Sans", 20,"italic"))
        t.up()
        t.goto(.3*cellSize,cellSize+30)
        t.down()
        t.write(userName2 + " (O):  " + str(scoreO), font=("Open Sans", 20,"italic"))
        
        session = playTTT(t,s,gameBoard,XWins,OWins)

        if (session == 'draw'):
            scoreX += 0
            scoreO += 0
        elif (session == 'Session complete! X won'):
            scoreX += 1
        elif (session == 'Session complete! O won'):
            scoreO += 1
        
        t.color('white')
        t.up()
        t.goto(-1.1*cellSize,cellSize+30)
        t.down()
        t.write(userName1 +  " (X):  " + str(scoreX), font=("Open Sans", 20,"italic"))
        t.up()
        t.goto(.3*cellSize,cellSize+30)
        t.down()
        t.write(userName2 +  " (O):  " + str(scoreO), font=("Open Sans", 20,"italic"))
        
        scoreX = int(scoreX)
        scoreO = int(scoreO)
        
        if (scoreO == int(getNumSessions)):
            print("All games over - O Won!")
            s.clear()
            gameOver(t,s)
            showOneWinner = 'o is the final winner'
            return showOneWinner    
        
        elif (scoreX == int(getNumSessions)):
            print("All games over - X Won!")
            s.clear()
            gameOver(t,s)
            showOneWinner = 'x is the final winner'
            return showOneWinner
        
        gameBoard = ['-','-','-','-','-','-','-','-','-']
        s.ontimer(writeCells(),2000)
        s.clear()

def gameControl(s):
    showOneWinner = continuePlay(t,s,scoreX,scoreO,gameBoard,promptX,promptO)
    if (showOneWinner == 'o is the final winner'):
        showWinnerO(t,showOneWinner)
        displayWinner = userName2
        return displayWinner
    elif(showOneWinner == 'x is the final winner'):
        showWinnerX(t,showOneWinner)
        displayWinner = userName1
        return displayWinner
    
    s.ontimer(writeCells(),2000)
    s.clear()
    
def collectRankings():
    list1 = []
    list2 = []
    list3 = []
    theNetTime = time.time()
    theNetTime = theNetTime/100000000
    theNetTime = round(theNetTime,7)
    playTime = "%s seconds" % (theNetTime)
    d = [list3,list1,list2]
    export_data = zip_longest(*d, fillvalue = '')
    
    displayWinner = gameControl(s)
    
    if (displayWinner == userName1):
        list1.append(displayWinner + " (X)")
        list2.append(getNumSessions)
        list3.append(playTime)
    elif (displayWinner == userName2):
        list1.append(displayWinner + " (O)")
        list2.append(getNumSessions)
        list3.append(playTime)
        
    #uncomment these 4 lines when starting a brand new csv file
    '''
    with open('ranks.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        fieldnames = ['Best Time','Username','Winning Score']
        thewriter = csv.DictWriter(myfile, fieldnames=fieldnames)
        thewriter.writeheader()
    '''
    with open('ranks.csv', 'a', encoding="ISO-8859-1", newline='') as myfile: 
        print(playTime)
        wr = csv.writer(myfile)
        wr.writerows(export_data)

    myfile.close()

def showRankings(t,s):
    s.bgcolor('black')
    t.up()
    t.goto(3*cellSize,3*cellSize)
    df = pandas.read_csv('ranks.csv')
    rslt_df = df.sort_values(by = 'Best Time')
    print(rslt_df)
    t.up()
    t.goto(0,cellSize/4)
    s.register_shape("ezgif.com-apng-to-gif.gif")
    t.shape("ezgif.com-apng-to-gif.gif")
    t.color('black')
    t.speed('slow')
    t.left(90)
    t.goto(1.8*cellSize,cellSize/4)
    t.goto(cellSize/4,-cellSize/2)
    t.up()
    t.color('white')
    t.goto(-0.5*cellSize,-1.34*cellSize)
    t.down()
    t.write(rslt_df, font=("Open Sans",10,"italic"))
    playsound("file:///Users/priscillamaryanski/Desktop/project-x-repo/game-over.mp3")
    t.up()
  
def everythingBagel():
    start_time = time.time()
    collectRankings()
    showRankings(t,s)

everythingBagel()