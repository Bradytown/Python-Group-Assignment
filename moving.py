import pygame, gameGlobals
from pygame.locals import *
from colliding import colliding
pygame.init()

class moving(colliding):

    def __init__(self,x,y,image):    
        colliding.__init__(self,x,y,image)
