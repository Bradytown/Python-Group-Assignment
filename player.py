#Player Class File
import pygame
from pygame.locals import *
from entity import entity
from gameGlobals import xOrig, yOrig
pygame.init()

class player(entity):

    def __init__(self,x,y,image):    
        entity.__init__(self,x,y,image)
