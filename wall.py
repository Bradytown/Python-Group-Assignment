import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class wall(entity):

    def __init__(self,x,y,image):    
        entity.__init__(self,x,y,image)
