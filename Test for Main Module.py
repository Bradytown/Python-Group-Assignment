import pygame, mainModule
from pygame.locals import *
from mainModule import refreshScreen, setBackgroundImage

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

setBackgroundImage("forest.jpg")

mainModule.init(screen)

while True:

    mainModule.refreshScreen()
