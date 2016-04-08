import pygame, gameGlobals
from pygame.locals import *
from moving import moving
from math import cos, sin
pygame.init()

class bullet(moving):

    def __init__(self,x,y,image, theta, vel, direction, shooter):    
        moving.__init__(self,x,y,image)
        self.theta = theta
        self.vel = vel
        self.direction = direction
        self.shooter = shooter

    
    def move(self):

        if self.direction == "right":
            self.x += cos(self.theta)*self.vel
            self.y += sin(self.theta)*self.vel
        else:
            self.x -=  cos(self.theta)*self.vel
            self.y -= sin(self.theta)*self.vel

    def update(self):
        self.move()
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig
        
