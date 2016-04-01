import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class gamePlatform(entity):

    def __init__(self, x, y, image):
        entity.__init__(self, x, y, image)

