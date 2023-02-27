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

floor = Sprite(0,350,400, 100, True, (0,255,0))
floor1 = Sprite(400,300,400,100, True, (0,255,0))
gravity = 1

ground.append(floor)
ground.append(floor1)


yVelocity = 0

xVelocity = 0
grounded = False
grounded1 = False

while run:

    screen.fill(0)
    player.draw((player.rect.x + xVelocity,player.rect.y + yVelocity))

    floor.draw()
    floor1.draw()
    yVelocity = gravity

    
    grounded = floor.rect.collidepoint(player.rect.x,player.rect.bottom+ 1)

    grounded1 = floor1.rect.collidepoint(player.rect.x, player.rect.bottom +1)

    if player.rect.collideobjects(ground):
        yVelocity = 0
    else:
        yVelocity = gravity
    if player.rect.colliderect((floor1.rect.x, floor1.rect.y), floor1.size):
        for i in ground:
            if i.rect.collidepoint(player.rect.y, player.rect.left):
                if xVelocity == -1:
                    xvelocity =0
            if i.rect.collidepoint(player.rect.y, player.rect.right):
                pass

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and (grounded or grounded1):
                for i in range(100):
                    player.draw((player.rect.x+xVelocity, player.rect.y + -1))
                    pygame.display.update()
                    screen.fill(0)
                    floor.draw()
                    floor1.draw()
                    time.sleep(0.005)
            if event.key == pygame.K_LEFT:
                xVelocity = -1
            if event.key == pygame.K_RIGHT:
                xVelocity = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                xVelocity = 0
    
    time.sleep(0.005)
    pygame.display.update()

pygame.quit()