import pygame
import time
pygame.init()

screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)

run = True



class Sprite(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, sizeX, sizeY, center = False, color = (0,0,255)):
        pygame.sprite.Sprite.__init__(self)
        self.size = (sizeX, sizeY)
        self.xpos = xpos
        self.ypos = ypos
        self.pos = (xpos, ypos)
        self.color = color

        self.rect = pygame.rect.Rect(self.pos,(sizeX, sizeY))
        if center:
            self.center = self.rect.center
    def draw(self, pos = (0,0)):
        if pos != (0,0):
            self.rect = pygame.rect.Rect(pos,self.size)
        pygame.draw.rect(screen, self.color, self.rect)

player = Sprite(100,100,30,30)

ground = []

wallsR = []
wallsL = []

floor = Sprite(0,350,400, 100, True, (0,255,0))
floor1 = Sprite(400,300,400,100, True, (0,255,0))
floor2 = Sprite(800, 350, 400,100, True, (0,255,0))
gravity = 1

ground.append(floor)
ground.append(floor1)
ground.append(floor2)

wallsR.append(pygame.rect.Rect(floor1.rect.right, floor1.rect.y, 1, floor1.rect.height)) 
wallsL.append(pygame.rect.Rect(floor1.rect.left, floor1.rect.y, 1, floor1.rect.height)) 
wallsR.append(pygame.rect.Rect(floor2.rect.right, floor2.rect.y, 1, floor2.rect.height)) 
wallsL.append(pygame.rect.Rect(floor2.rect.left, floor2.rect.y, 1, floor2.rect.height)) 
wallsR.append(pygame.rect.Rect(floor.rect.right, floor.rect.y, 1, floor.rect.height)) 
wallsL.append(pygame.rect.Rect(floor.rect.left, floor.rect.y , 1, floor.rect.height))


yVelocity = 0

xVelocity = 0
grounded = False
grounded1 = False
isJumping = False
jumpItteration = 0

while run:

    screen.fill(0)
    player.draw((player.rect.x + xVelocity,player.rect.y + yVelocity))

    for i in ground:
        i.draw()
    yVelocity = gravity

    if player.rect.collideobjects(ground):
        yVelocity = 0
        grounded = True
    else:
        yVelocity = gravity
    if player.rect.collideobjects(wallsR):
        if xVelocity == 1:
            xVelocity = 0
    for wall in wallsL:
        if wall.collidepoint(player.rect.x, player.rect.y):
            if xVelocity == -1:
                xVelcoity = 0

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (grounded or grounded1):
                if not isJumping:
                    isJumping = True
                    print('jumping')
                if ((isJumping) and (jumpItteration <= 300)):
                    yVelocity = -1
                    time.sleep(0.005)
                    jumpItteration+=1
                    print("jumped")
                else:
                    jumpItteration = 0
                    isJumping = False
            if event.key == pygame.K_LEFT:
                xVelocity = -1
            if event.key == pygame.K_RIGHT:
                xVelocity = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                xVelocity = 0
    
    time.sleep(0.005)
    pygame.display.update()
    print(jumpItteration <= 300)
    print(jumpItteration)
pygame.quit()