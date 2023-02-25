
#all the imports
import pygame
import random
import time
import pickle as pkl
import ClearHiScore
import GetHiScore

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
gameoverMusic = pygame.mixer.Sound("Data/Music/gameOver.wav")


#screen init
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Apple Clicker')

#enemy class for drawing the apple
class Sprite(pygame.sprite.Sprite):
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
Apple = Sprite(300,300,2,"Data/img/apple.png")
Fullscreen = Sprite(300, 300, 0.3, "Data/img/Fullscreen.png")
defualt = pygame.font.SysFont('Comic Sans MS', 20)
end = pygame.font.SysFont("Comic Sans MS", 30)
endScreenTxtSurface = end.render("""Game Over! Resetting Score! (Click To Dismiss)""",False,(255,255,255))
endScreentxtRect = endScreenTxtSurface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
#several variables for thegame to run properly
gameover = False
fullscreen = False
clickTime = 0
currentTime = time.time()
lowestClickTime = 10
hightstClickTime = 0
run = True
score = 0
sessionHi = 0
#pickle import for alltime hi score
alltimeHi = pkl.load(open("Data/hiScore.txt", 'rb'))
BGMusic.play(loops = -1)
#main loop
while run:
    SCREEN_HEIGHT = screen.get_height()
    SCREEN_WIDTH = screen.get_width()
    endScreentxtRect = endScreenTxtSurface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    currentTime = time.time()    
    scoreTxt = defualt.render(f"Current Score {score},",False,(255,255,255))
    sessionHiScoreTxt = defualt.render(f"Session Hi Score: {sessionHi},", False, (255,255,255))
    alltimeHiScoreTxt = defualt.render(f"All time Hi Score: {alltimeHi}.", False, (255,255,255))
    #screen and text init
    screen.fill(0)
    screen.blit(Apple.image, Apple.rect)
    screen.blit(scoreTxt, (10, 10))
    screen.blit(sessionHiScoreTxt, ((scoreTxt.get_width() + 20), 10))
    screen.blit(alltimeHiScoreTxt, (((sessionHiScoreTxt.get_width() + 20)+(scoreTxt.get_width() + 10)), 10)) 
    screen.blit(Fullscreen.image, ((screen.get_width() - Fullscreen.rect.width), 0))
    #event handeler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        pos = pygame.mouse.get_pos()
        pressed1 = pygame.mouse.get_pressed()[0]
        if event.type == pygame.MOUSEBUTTONDOWN:
        # Check if rectangle collided with pos and if the left mouse button was pressed
            if Apple.rect.collidepoint(pos) and pressed1:
                Apple.setPos(random.randint(100, screen.get_width() - 100),random.randint(100, screen.get_height() - 100))
                score +=1
                popSFX.play()
                clickTime = time.time()
            elif pressed1 and not Apple.rect.collidepoint(pos) and not Fullscreen.rect.collidepoint(pos):
                BGMusic.set_volume(0)
                gameoverMusic.play()
                gameover=True 
            elif gameover:
                gameover=False
                BGMusic.set_volume(100)
            if Fullscreen.rect.collidepoint(pos) and pressed1:
                fullscreen != fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)
        if event.__str__() == "<Event(771-TextInput {'text': 'p', 'window': None})>":
            score, sessionHi, alltimeHi = ClearHiScore.mainLoop()
            print('deleted Hi Score!')
        if event.__str__() == "<Event(771-TextInput {'text': 'h', 'window': None})>":
            GetHiScore.mainLoop()
    if score > alltimeHi:
        alltimeHi = score
    if score > sessionHi:
        sessionHi = score
    if gameover :
        screen.blit(endScreenTxtSurface, endScreentxtRect)
        Apple.setPos(random.randint(100, SCREEN_WIDTH - 100),random.randint(100,SCREEN_HEIGHT - 100))
        score = 0
        time.sleep(0.3)
    pygame.display.update()
pkl.dump(alltimeHi,open('Data/hiScore.txt','wb'))
pygame.quit()
