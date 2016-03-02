#Main module to import when you start programming

import pygame
from pygame.locals import *

def init(scr):
    screen = scr

def refreshScreen():
    screen.blit(background,(0,0))
    pygame.display.flip()

def setBackgroundImage(image):
    background = pygame.image.load(image)

