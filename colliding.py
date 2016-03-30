import pygame, gameGlobals
from pygame.locals import *
from entity import entity
pygame.init()

class colliding(entity):

    def __init__(self,x,y,image):    
        entity.__init__(self,x,y,image)
        self.acc = 0.2
        self.affectedByGravity=False
        self.direction = "left"

    def gravity(self,x):
        if x:
            print("True")
            self.fallSpeed=0
            self.affectedByGravity=True
        else:
            print("False")
            self.affectedByGravity=False

    def flip(self):
        if self.direction == "left":
            self.direction = "right"
        else:
            self.direction = "left"

        self.image = pygame.transform.flip(self.image, True, False)

    def update(self):

        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig
