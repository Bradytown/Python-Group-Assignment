#Player Class File
import pygame, gameGlobals
from pygame.locals import *
from colliding import colliding
pygame.init()

class player(colliding):

    def __init__(self,x,y,image):    
        colliding.__init__(self,x,y,image)

    
    def update(self):

        gameGlobals.playerX = self.x
        gameGlobals.playerY = self.y
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        
