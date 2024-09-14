from tkinter import *
from time import sleep
from game_objects import setInitialValues, drawIntro, drawObjects, generateBlocks, drawBlocks, updateObjects
from collisions import (detectBlockCollisions, detectPlateCollision, detectFirstWallCollision,
                        detectSecondWallCollision, detectCeilingCollision, changeBallBlockDirection,
                        changeBallPlateDirection, changeBallBordersDirection)
from input_handlers import mouseClickHandler, keyDownHandler, keyUpHandler
from ui import endGame

root = Tk()
screen = Canvas(root, width=1000, height=1000, background="black")

def runGame():
    global failedGame
    setInitialValues()
    screen.update()
    firstTime = True

    while True:
        if introScreen:
            drawIntro(screen)
            screen.update()
            sleep(0.03)
            screen.delete("all")  # Clear intro screen
        else:
            if firstTime:
                xBlocks, yBlocks, xSizeBlocks, ySizeBlocks = generateBlocks()
                drawBlocks(screen, xBlocks, yBlocks, xSizeBlocks, ySizeBlocks)
                firstTime = False

            drawObjects(screen)
            updateObjects()

            if yBall < blocksUpperLimit + 20:
                blockCollision = detectBlockCollisions(xBall, yBall, xBlocks, yBlocks, xSizeBlocks, ySizeBlocks)
                if blockCollision != "noCollision":
                    changeBallBlockDirection(blockCollision)

            if yBall > yPlate - 20:
                plateCollision = detectPlateCollision(xBall, yBall)
                if plateCollision:
                    changeBallPlateDirection(plateCollision)

            wallNumber = 0
            if xBall < xFirstWall + 40:
                wallNumber = detectFirstWallCollision(xFirstWall, yFirstWall, xBall, yBall)
                if wallNumber == 1:
                    changeBallBordersDirection(wallNumber)
            elif xBall > xSecondWall - 40:
                wallNumber = detectSecondWallCollision(xSecondWall, ySecondWall, xBall, yBall)
                if wallNumber == 2:
                    changeBallBordersDirection(wallNumber)

            if yBall < yCeiling + 40:
                wallNumber = detectCeilingCollision(xCeiling, yCeiling, xBall, yBall)
                if wallNumber == 3:
                    changeBallBordersDirection(wallNumber)

            if yBall >= 1000:
                failedGame = True
                endGame(screen, score)
                screen.delete("all")
                screen.update()
                break

            screen.update()
            sleep(0.03)
            screen.delete("all")

root.after(1000, runGame)
screen.bind("<Button-1>", mouseClickHandler)
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
screen.focus_set()
root.mainloop()
