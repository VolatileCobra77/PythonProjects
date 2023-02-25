import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), pygame.RESIZABLE)

class enemy(pygame.sprite.Sprite):
    def __init__(self, RectHeight, RectWidth, RectX, RectY, dmg = 12):
        pygame.sprite.Sprite.__init__(self)
        self.dmg = dmg
        self.pos = (RectX, RectY)
        charRect = pygame.rect.Rect(RectX, RectY, RectWidth, RectHeight)
        self.character = pygame.draw.rect(screen, (255,0,0), charRect)

class player(pygame.sprite.Sprite):
    def __init__(self, RectHeight, RectWidth, RectX, RectY):
        pygame.sprite.Sprite.__init__(self)
        self.pos = (RectX, RectY)
        self.size = (RectWidth, RectHeight)
        self.width = RectWidth
        self.height = RectHeight
        self.x = RectX
        self.y = RectY
        self.charRect = pygame.rect.Rect(RectX, RectY, RectWidth, RectHeight)
    def draw(self):
        pygame.draw.rect(screen, (0,255,0), self.charRect)
    def newPos(self, newX = 0, newY = 0):
        charrect = pygame.rect.Rect(newX, newY, self.width, self.height)
        self.charRect = charrect

bgColor = (100,100,255)
playerHealth = 100
playerObj = player(30, 30, 100, 500)
defualtFont = pygame.font.SysFont("Comic Sans MS", 30)
scene = 0
gravity = 1
xVelocity = 0
yVelocity = 0
run = True
isJumping = False


while run:
    

    SCREEN_HEIGHT = screen.get_height()
    SCREEN_WIDTH = screen.get_width()

    screen.fill(bgColor)
    playerObj.draw()

    if playerObj.charRect.top<0:
        playerObj.charRect.top = (0)
    elif playerObj.charRect.bottom > SCREEN_HEIGHT:
        playerObj.charRect.bottom = SCREEN_HEIGHT


    #event handeler
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xVelocity = -1
                
            elif event.key == pygame.K_RIGHT:
                xVelocity = 1
                playerObj.newPos((playerObj.charRect.x + xVelocity), playerObj.charRect.y)
            if event.key == pygame.K_UP:
                yVelocity = -1
                gravity = 0
            elif event.key == pygame.K_DOWN:
                playerObj.newPos(100,100)
                playerObj.draw()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xVelocity = 0
            if event.key == pygame.K_UP:
                yVelocity = 0
                gravity = 1
    playerObj.newPos((playerObj.charRect.x + xVelocity), ((playerObj.charRect.bottom + gravity) +  yVelocity))           
    pygame.display.update()
    #time.sleep(0.0001)
pygame.quit()