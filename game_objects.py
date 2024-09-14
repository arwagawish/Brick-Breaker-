from random import randint, choice

def setInitialValues():
    global score, xBall, yBall, diameter, xSpeed, ySpeed, xPlate, yPlate, xPlateSpeed
    global xFirstWall, yFirstWall, xSecondWall, ySecondWall, xCeiling, yCeiling
    global introScreen, failedGame, blocksUpperLimit, blocksLowerLimit, plateColour
    
    score = 0
    xBall, yBall = 500, 500
    diameter, xSpeed, ySpeed = 20, -5, -8
    xPlate, yPlate, xPlateSpeed = 500, 800, 0
    xFirstWall, yFirstWall, xSecondWall, ySecondWall = 0, 0, 980, 0
    xCeiling, yCeiling = 20, 0
    blocksLowerLimit, blocksUpperLimit = 100, 200
    plateColour = "red"
    introScreen, failedGame = True, False

def drawIntro(screen):
    intro1 = screen.create_text(500, 500, text="SPEEDY PONG", font="Times 40", fill="white")
    intro2 = screen.create_text(480, 600, text="Use the arrow keys to move the plate.", font="Times 15", fill="white")
    intro3 = screen.create_text(500, 700, text="Click Anywhere to Continue", font="Times 30", fill="white")

def generateBlocks(numOfBlocks=6):
    xBlocks, yBlocks = [None] * numOfBlocks, [None] * numOfBlocks
    xSizeBlocks, ySizeBlocks = [None] * numOfBlocks, [None] * numOfBlocks
    xSpacing = int(1000 / numOfBlocks)
    
    for i in range(numOfBlocks):
        xBlocks[i] = randint(i * xSpacing, i * xSpacing + xSpacing)
        yBlocks[i] = randint(100, 200)
        xSizeBlocks[i] = randint(40, 200)
        ySizeBlocks[i] = randint(20, 40)
        
    return xBlocks, yBlocks, xSizeBlocks, ySizeBlocks

def drawBlocks(screen, xBlocks, yBlocks, xSizeBlocks, ySizeBlocks):
    for i in range(len(xBlocks)):
        screen.create_rectangle(xBlocks[i], yBlocks[i], xBlocks[i] + xSizeBlocks[i], yBlocks[i] + ySizeBlocks[i], fill="red")

def drawObjects(screen):
    global ballDrawing, plateDrawing, firstWallDrawing, secondWallDrawing, ceilingDrawing, scoreCount
    
    ballDrawing = screen.create_oval(xBall, yBall, xBall + diameter, yBall + diameter, fill="red")
    plateDrawing = screen.create_rectangle(xPlate, yPlate, xPlate + 200, yPlate + 50, fill=plateColour)
    firstWallDrawing = screen.create_rectangle(0, 0, 20, 1000, fill="red")
    secondWallDrawing = screen.create_rectangle(980, 0, 1000, 1000, fill="red")
    ceilingDrawing = screen.create_rectangle(20, 0, 980, 20, fill="red")
    scoreCount = screen.create_text(100, 50, text="Score: " + str(score), font="Arial 20", fill="white")

def updateObjects():
    global xBall, yBall, xSpeed, ySpeed, xPlate, xPlateSpeed
    xBall += xSpeed
    yBall += ySpeed
    xPlate += xPlateSpeed
