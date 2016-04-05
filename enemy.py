#Enemy Class File
import pygame, gameGlobals
from pygame.locals import *
from moving import moving
pygame.init()

class enemy(moving):

    def __init__(self,x,y,image):    
        moving.__init__(self,x,y,image)

    def update(self):

        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig
        
        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc

