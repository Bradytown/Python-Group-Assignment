import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class gamePlatform(entity):

    def __init__(self, x, y, length, centreImage, leftImage, rightImage, screen):
        entity.__init__(self, x, y, centreImage, screen)
        self.leftImage = pygame.image.load(leftImage)
        self.rightImage = pygame.image.load(rightImage)
        self.centreImage = pygame.image.load(centreImage)
        self.length = length

        if self.length < 0:
            self.length = 0

    def refresh(self):

        self.screen.blit(self.leftImage, (self.x, self.y))

        dx = 0
        
        for i in range (0,self.length):

            if i == 0:
                dx += int(self.leftImage.get_width())
            else:
                dx += int(self.centreImage.get_width())

            self.screen.blit(self.centreImage, (self.x+dx, self.y))

        dx += int(self.centreImage.get_width())
        self.screen.blit(self.rightImage,(self.x+dx, self.y))
