import pygame, gameGlobals
from pygame.locals import *
from moving import moving
pygame.init()

class bullet(moving):

    def __init__(self,x,y,image):    
        moving.__init__(self,x,y,image)
