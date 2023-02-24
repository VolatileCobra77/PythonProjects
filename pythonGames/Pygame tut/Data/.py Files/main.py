import pygame
import random
import time
import pickle as pkl
pygame.init()
pygame.font.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Apple Clicker')

class enemy(pygame.sprite.Sprite):
    def __init__(self, x,y, scale, imagePath):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(imagePath)
        sizeX = int(img.get_height()) * scale
        sizeY = int(img.get_width()) * scale
        self.image = pygame.transform.scale(img, (int(sizeY),int(sizeX)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def set_X(self,newX):
        self.rect.x = newX
    def set_Y(self,newY):
        self.rect.y = newY
    def setPos(self,newX,newY):
        self.rect.x = newX
        self.rect.y = newY

x= 200
y=200

enemy1 = enemy(300,300,2,"Data/img/apple.png")
defualt = pygame.font.SysFont('Comic Sans MS', 20)
end = pygame.font.SysFont("Comic Sans MS", 50)
endScreenTxtSurface = end.render("Game Over! Resetting Score!(Click To Dismiss)",False,(255,255,255))
endScreentxtRect = endScreenTxtSurface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
gameover = False
run = True
score = 0
sessionHi = 0
alltimeHi = pkl.load(open("Data/hiScore.txt", 'rb'))

while run:

    screen.fill(0)
    screen.blit(enemy1.image, enemy1.rect)
    scoreTxt = defualt.render(f"Current Score {score}",False,(255,255,255))
    sessionHiScoreTxt = defualt.render(f"Session Hi Score: {sessionHi}", False, (255,255,255))
    alltimeHiScoreTxt = defualt.render(f"All time Hi Score: {alltimeHi}", False, (255,255,255))
    screen.blit(scoreTxt, (10, 10))
    screen.blit(sessionHiScoreTxt, (10, 45))
    screen.blit(alltimeHiScoreTxt, (10, 90))



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
