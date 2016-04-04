#Enemy Class File
import pygame
from pygame.locals import *
from moving import moving
pygame.init()

class enemy(moving):

    def __init__(self,x,y,image):    
        moving.__init__(self,x,y,image)

    def update(self):
        
        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc

        gameGlobals.enemyX = self.x
        gameGlobals.enemyY = self.y
