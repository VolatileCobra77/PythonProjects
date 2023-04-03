from settings import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = playerPos
        self.angle = playerAngle


    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy = 0,0
        speed = playerSpeed * self.game.deltaTime
        speedSin = speed *sin_a
        speedCos = speed * cos_a

        key =  pg.key.get_pressed()
        if  key[pg.K_w]:
            dx += speedCos
            dy += speedSin
        if key[pg.K_s]:
            dx += -speedCos
            dy += -speedSin
        if key[pg.K_a]:
            dx += speedSin
            dy += - speedCos
        if key[pg.K_d]:
            dx += -speedSin
            dy += speedCos

        self.checkWallCollision(dx, dy)

        if key[pg.K_LEFT]:
            self.angle -= playerRotSpeed *self.game.deltaTime
        
        if key[pg.K_RIGHT]:
            self.angle += playerRotSpeed *self.game.deltaTime
        self.angle %= math.tau

    def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), (self.x * 100 + WIDTH * math.cos(self.angle), self.y *100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x *100, self.y * 100), 15)

    def checkWall(self, x, y):
        return (x,y) not  in self.game.map.world_map
    def checkWallCollision(self, dx, dy):
        if self.checkWall(int(self.x +dx), int(self.y)):
            self.x += dx
        if self.checkWall(int(self.x), int(self.y + dy)):
            self.y += dy


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    @property
    def map_pos(self):
        return int(self.x), int(self.y)