#Player Class File
import pygame, gameGlobals
from pygame.locals import *
from colliding import colliding
pygame.init()

class player(colliding):

    def __init__(self,x,y,image):    
        colliding.__init__(self,x,y,image)

    
    def update(self):

        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc

        gameGlobals.playerX = self.x
        gameGlobals.playerY = self.y
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        
