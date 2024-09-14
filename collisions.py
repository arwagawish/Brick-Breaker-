def detectBlockCollisions(xBall, yBall, xBlocks, yBlocks, xSizeBlocks, ySizeBlocks):
    limit = 15
    centreBall = [xBall + 10, yBall + 10]
    
    for i in range(len(xBlocks)):
        if yBlocks[i] < centreBall[1] < yBlocks[i] + limit and xBlocks[i] < centreBall[0] < xBlocks[i] + xSizeBlocks[i]:
            return "Top"
        elif yBlocks[i] + ySizeBlocks[i] - limit < centreBall[1] < yBlocks[i] + ySizeBlocks[i]:
            return "Bottom"
        elif xBlocks[i] < centreBall[0] < xBlocks[i] + limit and yBlocks[i] < centreBall[1] < yBlocks[i] + ySizeBlocks[i]:
            return "Left"
        elif xBlocks[i] + xSizeBlocks[i] - limit < centreBall[0] < xBlocks[i] + xSizeBlocks[i]:
            return "Right"
    return "noCollision"

def detectPlateCollision(xBall, yBall):
    global xPlate, yPlate, score, plateColour
    centreBall = [xBall + 10, yBall + 10]
    
    if xPlate <= centreBall[0] <= xPlate + 200 and yPlate <= centreBall[1] <= yPlate + 50:
        score += 1
        plateColour = choice(["blue", "green", "yellow", "purple", "pink", "orange", "brown"])
        return True
    return False

def detectFirstWallCollision(xFirstWall, yFirstWall, xBall, yBall):
    centreBall = [xBall + 10, yBall + 10]
    if centreBall[0] <= xFirstWall + 20:
        return 1
    return 0

def detectSecondWallCollision(xSecondWall, ySecondWall, xBall, yBall):
    centreBall = [xBall + 10, yBall
