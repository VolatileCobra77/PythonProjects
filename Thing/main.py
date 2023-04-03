import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(res, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.deltaTime = 1
        self.new_game()

    def new_game(self):
        self.map = map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)

    def update(self):
        self.raycasting.update()
        pg.display.flip()
        
        self.player.update()
        self.deltaTime = self.clock.tick(FPS)
        pg.display.set_caption(f"{self.clock.get_fps() : .1f}")

    def draw(self):
        self.screen.fill('black')
        
        self.player.draw()
        
        self.map.draw()
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    
    def run(self):
        while True:
            self.check_events()
           
            self.draw()
            self.update()

if __name__ == "__main__":
    game=Game()
    game.run()