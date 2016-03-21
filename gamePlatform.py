import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class gamePlatform(entity):

    def __init__(self, x, y, length, image):
        entity.__init__(self, x, y, image)

##        self.leftImage = pygame.image.load(leftImage)
##        self.rightImage = pygame.image.load(rightImage)
##        self.centreImage = pygame.image.load(centreImage)
        self.length = length

        if self.length <= 0:
            self.length = 1
