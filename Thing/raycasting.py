import pygame as pg
import math
from settings import *


class Raycasting:
    def __init__(self, game):
        self.game = game


    def raycast(self):
        ox, oy = self.game.player.pos
        xMap, yMap = self.game.player.map_pos

        rayAngle = self.game.player.angle - halfFOV + 0.0001
        for ray in range(numrays):
            sin_a = math.sin(rayAngle)
            cos_a = math.cos(rayAngle)


            yhor, dy = (xMap+1,1 )  if cos_a>0 else (xMap - 1e-6, -1)

            depthor = (yhor - oy) / cos_a
            xhor = ox + depthor *sin_a

            deltaDepth = dy/sin_a
            dx = deltaDepth * cos_a
            for i in range(maxDepth):
                tile_hor = int(xhor), int(yhor)
                if tile_hor in self.game.map.world_map:
                    break
                xhor +=dx
                yhor +=dy
                depthor += deltaDepth

            #verts
            xvert, dx = (xMap+1,1 )  if cos_a>0 else (xMap - 1e-6, -1)

            depthVert = (xvert - ox) / cos_a
            yvert = oy + depthVert *sin_a

            deltaDepth = dx/cos_a
            dy = deltaDepth * sin_a

            for i in range(maxDepth):
                tile_vert = int(xvert), int(yvert)
                if tile_vert in self.game.map.world_map:
                    break
                xvert +=dx
                yvert +=dy
                depthVert += deltaDepth

            

            if depthVert < depthor:
                depth = depthVert
            else:
                depth = depthor
            
            pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy), (100*ox +100 * depth * cos_a, 100*oy +100 * depth * sin_a),2)
            rayAngle += deltaAngle
    def update(self):
        self.raycast()