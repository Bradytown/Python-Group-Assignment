#Main module to import when you start programming

import pygame
from pygame.locals import *

def __init__(screen):
    self.screen = screen

def refreshScreen():
    self.screen.blit(background,(0,0))
    pygame.display.flip()

def setBackgroundImage(image):
    self.background = pygame.image.load(image)
