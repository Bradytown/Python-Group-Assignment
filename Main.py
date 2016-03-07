#Main module to import when you start programming
#Doesn't do anything yet

import pygame
from pygame.locals import *
from player import *

pygame.init()

size = screenHeight, screenWidth = 640, 480

screen = pygame.display.set_mode(size)


def mainMenu():

    print ("This is where the main menu will run")

def game():

    playerImage = "square.png"
    
    player1 = player(100,100,playerImage,screen)

    while True:
        screen.fill((0,0,0))
        player1.refresh()
        pygame.display.flip()

game()
