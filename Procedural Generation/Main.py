import pygame
from enum import Enum
from pygame.locals import QUIT
import random

SCREENWIDTH = 400
SCREENHEIGHT = 400

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Hello World!')

noGen = False
maxYLen = 40
maxXLen = 40
GREY = (30, 30, 30)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
player = (0, 0, 0, 0)
sameGenChance = 89

def genTerrain(tileList, colorList, pos):
        neighbours = []
        colors = {}
        for valid in VALID_TERRAINS:
                colors[valid] = 0
        for i in range(pos[0] -1, pos[0]+2):
                for j in range(pos[1]-1, pos[1]+2):
                        if i > 0 and i < maxXLen-1 and j >0 and j < maxYLen -1:
                                neighbours.append(colorList[i][j])
                        else:
                                neighbours.append(randomTerrain())

        for neighbour in neighbours:
                
                if neighbour != terrain.UNDEFINED:
                        colors[neighbour] += 1
        currentColor = None
        prevHigh = 0

        for color in colors:
                if colors[color] > prevHigh:
                        prevHigh = colors[color]
                        currentColor = color
                        
        percent = random.randint(0, 100)
        gen = True
        if percent >= sameGenChance and gen:
                val = randomTerrain()
        else:
                val = currentColor
                
        return val
class terrain(Enum):
    UNDEFINED = 0
    RED = 1
    GREEN = 2
    BLUE = 3


VALID_TERRAINS = []
for terr in terrain:
    if (terr != terrain.UNDEFINED):
        VALID_TERRAINS.append(terr)

types = [terrain.RED, terrain.GREEN, terrain.BLUE]


class tile():
    tileSize = 10

    def __init__(self, pos, type=0):
        self.rect = ((pos[0] * self.tileSize, pos[1] * self.tileSize),
                     (self.tileSize, self.tileSize))
        self.x = pos[0]
        self.y = pos[1]
        if type == terrain.UNDEFINED:
            self.color = GREY
        elif type == terrain.RED:
            self.color = RED
        elif type == terrain.GREEN:
            self.color = GREEN
        elif type == terrain.BLUE:
            self.color = BLUE
        else:
            raise Exception("Un Acceptable Type Value")

    def draw(self):
        pygame.draw.rect(DISPLAYSURF, self.color, self.rect)

    def setpos(self, newPos):
        self.rect = (newPos, (self.tileSize, self.tileSize))

    def setType(self, newType):
        if newType == terrain.UNDEFINED:
            self.color = GREY
        elif newType == terrain.RED:
            self.color = RED
        elif newType == terrain.GREEN:
            self.color = GREEN
        elif newType == terrain.BLUE:
            self.color = BLUE
        else:
            raise Exception("Un Acceptable Type Value")

    def drawPlayer(self):
        pygame.draw.rect(DISPLAYSURF, WHITE,
                         (self.x * self.tileSize + int(self.tileSize / 4),
                          self.y * self.tileSize + int(self.tileSize / 4),
                          int(self.tileSize / 2), int(self.tileSize / 2)))

    def clearPLayer(self):
        self.draw()


running = True

level = []
squares = []

for i in range(maxYLen):
    level.append([])
    squares.append([])
    for j in range(maxXLen):
        level[i].append(terrain.UNDEFINED)
        squares[i].append(tile((i, j), terrain.UNDEFINED))


def randomTerrain():
    return random.choice(types)


def populateMiddle():
    mid = randomTerrain()
    x = int(maxXLen / 2)
    y = int(maxYLen / 2)
    level[y][x] = mid
    squares[y][x].setType(mid)
    squares[y][x].draw()
    squares[y][x].drawPlayer()
    return (x, y)


for i in range(maxYLen):
    for j in range(maxXLen):
        squares[i][j].draw()

currentPos = populateMiddle()

while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        running = False
                if event.type == pygame.KEYDOWN:
                        
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                                if currentPos[0] <= (maxXLen * -1):
                                        currentPos = (0,currentPos[1])
                                if currentPos[1]<=(maxYLen * -1):
                                        currentPos[1] = (currentPos[0], 0)
                                squares[currentPos[0]][currentPos[1]].draw()
                                squares[currentPos[0] - 1][currentPos[1]].drawPlayer()
                                currentPos = (currentPos[0] - 1, currentPos[1])
                                if level[currentPos[0]][currentPos[1]] == terrain.UNDEFINED:                      
                                   
                                    currentType = genTerrain(squares, level, currentPos)
                                    squares[currentPos[0]][currentPos[1]].setType(currentType)
                                    squares[currentPos[0]][currentPos[1]].draw()
                                    squares[currentPos[0]][currentPos[1]].drawPlayer()
                                    level[currentPos[0]][currentPos[1]] = currentType
        
                                        
                                        
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                if currentPos[0] <= (maxXLen * -1):
                                        currentPos = (0,currentPos[1])
                                if currentPos[1]<=(maxYLen * -1):
                                        currentPos[1] = (currentPos[0], 0)
                                squares[currentPos[0]][currentPos[1]].draw()
                                squares[currentPos[0] + 1][currentPos[1]].drawPlayer()
                                currentPos = (currentPos[0] + 1, currentPos[1])
                                if level[currentPos[0]][currentPos[1]] == terrain.UNDEFINED:                      
                                        
                                        currentType = genTerrain(squares, level, currentPos)
                                        squares[currentPos[0]][currentPos[1]].setType(currentType)
                                        squares[currentPos[0]][currentPos[1]].draw()
                                        squares[currentPos[0]][currentPos[1]].drawPlayer()
                                        level[currentPos[0]][currentPos[1]] = currentType
        
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                                if currentPos[0] <= (maxXLen * -1):
                                        currentPos = (0,currentPos[1])
                                if currentPos[1]<=(maxYLen * -1):
                                        currentPos[1] = (currentPos[0], 0)
                                squares[currentPos[0]][currentPos[1]].draw()
                                squares[currentPos[0]][currentPos[1]-1].drawPlayer()
                                currentPos = (currentPos[0], currentPos[1]-1)
                                if level[currentPos[0]][currentPos[1]] == terrain.UNDEFINED:                      
                                        
                                        currentType = genTerrain(squares, level, currentPos)
                                        squares[currentPos[0]][currentPos[1]].setType(currentType)
                                        squares[currentPos[0]][currentPos[1]].draw()
                                        squares[currentPos[0]][currentPos[1]].drawPlayer()
                                        level[currentPos[0]][currentPos[1]] = currentType
        
        
        
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                if currentPos[0] <= (maxXLen * -1):
                                        currentPos = (0,currentPos[1])
                                if currentPos[1]<=(maxYLen * -1):
                                        currentPos[1] = (currentPos[0], 0)
                                squares[currentPos[0]][currentPos[1]].draw()
                                squares[currentPos[0]][currentPos[1]+1].drawPlayer()
                                currentPos = (currentPos[0], currentPos[1]+1)
                                if level[currentPos[0]][currentPos[1]] == terrain.UNDEFINED:                      
                                        
                                        currentType = genTerrain(squares, level, currentPos)
                                        squares[currentPos[0]][currentPos[1]].setType(currentType)
                                        squares[currentPos[0]][currentPos[1]].draw()
                                        squares[currentPos[0]][currentPos[1]].drawPlayer()
                                        level[currentPos[0]][currentPos[1]] = currentType
        if not running:
                break
        pygame.display.update()
print("done")