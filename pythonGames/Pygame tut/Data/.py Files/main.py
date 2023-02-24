
#all the imports
import pygame
import random
import time
import pickle as pkl

#pygame, pygame font and pygame mixer initilizations
pygame.init()
pygame.font.init()
pygame.mixer.init()

#Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

#SFX initilization
popSFX = pygame.mixer.Sound("Data/Music/POP.mp3")
BGMusic = pygame.mixer.Sound("Data/Music/BGmusic.mp3")


#screen init
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Apple Clicker')

#enemy class for drawing the apple
class enemy(pygame.sprite.Sprite):
    def __init__(self, x,y, scale, imagePath):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imagePath)
        sizeX = int(img.get_height()) * scale
        sizeY = int(img.get_width()) * scale
        self.image = pygame.transform.scale(img, (int(sizeY),int(sizeX)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    #enemy.set_X(num) to set just the x value
    def set_X(self,newX):
        self.rect.x = newX
    #enemy.set_Y(num) to set just the y value
    def set_Y(self,newY):
        self.rect.y = newY
    #enemy.setPos(num,num2) to set both
    def setPos(self,newX,newY):
        self.rect.x = newX
        self.rect.y = newY

#enemy init
x= 200
y=200
enemy1 = enemy(300,300,2,"Data/img/apple.png")
defualt = pygame.font.SysFont('Comic Sans MS', 20)
end = pygame.font.SysFont("Comic Sans MS", 50)
endScreenTxtSurface = end.render("Game Over! Resetting Score!(Click To Dismiss)",False,(255,255,255))
endScreentxtRect = endScreenTxtSurface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
#several variables for thegame to run properly
gameover = False
run = True
score = 0
sessionHi = 0
#pickle import for alltime hi score
alltimeHi = pkl.load(open("Data/hiScore.txt", 'rb'))
pygame.mixer.music.play(BGMusic, loops= -1)
#main loop
while run:
    #screen and text init
    screen.fill(0)
    screen.blit(enemy1.image, enemy1.rect)
    scoreTxt = defualt.render(f"Current Score {score}",False,(255,255,255))
    sessionHiScoreTxt = defualt.render(f"Session Hi Score: {sessionHi}", False, (255,255,255))
    alltimeHiScoreTxt = defualt.render(f"All time Hi Score: {alltimeHi}", False, (255,255,255))
    screen.blit(scoreTxt, (10, 10))
    screen.blit(sessionHiScoreTxt, (10, 45))
    screen.blit(alltimeHiScoreTxt, (10, 90))


    #event handeler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if rectangle collided with pos and if the left mouse button was pressed
            if enemy1.rect.collidepoint(pos) and pressed1:
                enemy1.setPos(random.randint(100, SCREEN_WIDTH - 100),random.randint(100,SCREEN_HEIGHT - 100))
                score +=1
                popSFX.play()
            elif pressed1 and not enemy1.rect.collidepoint(pos):
                gameover=True
            elif gameover:
                gameover=False
    if score > alltimeHi:
        alltimeHi = score
    if score > sessionHi:
        sessionHi = score
    if gameover :
        screen.blit(endScreenTxtSurface, endScreentxtRect)
        enemy1.setPos(random.randint(100, SCREEN_WIDTH - 100),random.randint(100,SCREEN_HEIGHT - 100))
        score = 0
        time.sleep(0.3)
    pygame.display.update()
    pkl.dump(alltimeHi,open('Data/hiScore.txt','wb'))
pygame.quit()
