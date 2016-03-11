import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class gamePlatform(entity):

    def __init__(self, x, y, length, image, screen):
        entity.__init__(self, x, y, image, screen)

##        self.leftImage = pygame.image.load(leftImage)
##        self.rightImage = pygame.image.load(rightImage)
##        self.centreImage = pygame.image.load(centreImage)
        self.length = length

        if self.length <= 0:
            self.length = 1

    def refresh(self):


        self.dx = 0
        

        for i in range(0,self.length):
            self.screen.blit(self.image,(self.x+self.dx,self.y))
            self.dx+=int(self.image.get_width())

##        self.screen.blit(self.leftImage, (self.x, self.y))
##
##        dx = 0
##        
##        for i in range (0,self.length):
##
##            if i == 0:
##                dx += int(self.leftImage.get_width())
##            else:
##                dx += int(self.centreImage.get_width())
##
##            self.screen.blit(self.centreImage, (self.x+dx, self.y))
##
##        dx += int(self.centreImage.get_width())
##        
##        self.screen.blit(self.rightImage,(self.x+dx, self.y))
