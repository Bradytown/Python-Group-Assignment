#Enemy Class File
import pygame
from pygame.locals import *
from entity import entity
pygame.init()

class Enemy(entity):

    def __init__(self,x,y,image,screen):    
        entity.__init__(self,x,y,image,screen)
