import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class platform(entity):

    def __init__(self, x, y, length, centreImage, leftImage, rightImage, screen):
        entity.__init__(self, x, y, image, screen)
        self.leftImage = leftImage
        self.rightImage = rightImage
        self.centreImage = centreImage
        del(self.image)

        if length < 0:
            length = 0

    def refresh():

        self.screen.blit(self.leftImage, (self.x, self.y))

        dx = 0
        for i in range (0,length):

            if i == 0:
                dx += self.leftImage.get_width()
            else:
                dx += self.centerImage.get_width()

            self.screen.blit(self.centreImage, (self.x+dx, self.y))

        dx += self.centreImage.get_width
        self.screen.blit(self.rightImage,(self.x+dx, self.y))
