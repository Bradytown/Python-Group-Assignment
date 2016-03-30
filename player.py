#Player Class File
import pygame, gameGlobals
from pygame.locals import *
from colliding import colliding
from bullet import bullet
from math import atan, pi
pygame.init()

class player(colliding):

    def __init__(self,x,y,image,bulletImage,gunPos):    
        colliding.__init__(self,x,y,image)

        self.bulletImage = bulletImage
        self.gunPos = self.gunX, self.gunY = gunPos
        self.bulletVelocity = 5
    
    def update(self):

        if self.affectedByGravity:
            self.move (0,self.fallSpeed)
            self.fallSpeed += self.acc

        gameGlobals.playerX = self.x
        gameGlobals.playerY = self.y
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        
    def shoot(self):

        self.mousePos = self.mouseX, self.mouseY = pygame.mouse.get_pos()
        if (self.x-self.mouseX) == 0:
            if self.y-self.mouseY > 0:
                self.theta = 3*pi/2
            else:
                self.theta = pi/2
        else:
            self.theta = atan((self.y-self.mouseY)/(self.x-self.mouseX))


        if self.direction == "left":
            
            if self.mouseX > self.x + self.gunX:
                self.bulletDirection = "right"
            else:
                self.bulletDirection = "left"
                
            if (self.x-self.mouseX) == 0:
                if self.y-self.mouseY > 0:
                    self.theta = 3*pi/2
                else:
                    self.theta = pi/2
            else:
                self.theta = atan((self.y-self.mouseY)/(self.x-self.mouseX))
                
        else:
            
            if self.mouseX > self.x + self.width - self.gunX:
                self.bulletDirection = "right"
            else:
                self.bulletDirection = "left"

            print("WORK ON THIS HTING IN PLAYER")

            if (self.x-self.mouseX) == 0:
                if self.y-self.mouseY > 0:
                    self.theta = 3*pi/2
                else:
                    self.theta = pi/2
            else:
                self.theta = atan((self.y-self.mouseY)/(self.x-self.mouseX))

        if self.direction == "left":
            return bullet(self.x+self.gunX, self.y+self.gunY, self.bulletImage, self.theta, self.bulletVelocity, self.bulletDirection) 
        else:
            return bullet(self.x+self.width-self.gunX, self.y+self.gunY, self.bulletImage, self.theta, self.bulletVelocity, self.bulletDirection) 
        

    
