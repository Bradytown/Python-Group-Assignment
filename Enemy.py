#Enemy Class File
import pygame
from pygame.locals import *
from moving import moving
pygame.init()

class enemy(moving):

    def __init__(self,x,y,image):    
        moving.__init__(self,x,y,image)
