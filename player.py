#Player Class File
import pygame, gameGlobals
from pygame.locals import *
from colliding import colliding
from bullet import bullet
pygame.init()

class player(colliding):

    def __init__(self,x,y,image,bulletImage,gunPos):    
        colliding.__init__(self,x,y,image)

        self.bulletImage = bulletImage
        self.gunPos = self.gunX, self.gunY = gunPos
    
    def update(self):

        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc

        gameGlobals.playerX = self.x
        gameGlobals.playerY = self.y
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        
    def shoot(self):
        
        return bullet(self.x+self.gunX, self.y+self.gunY, self.bulletImage) 
    
