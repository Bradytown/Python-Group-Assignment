import pygame, time
from pygame.locals import *
from player import *
from gamePlatform import *

pygame.init()

size = screenWidth, screenHeight = 640, 480

screen = pygame.display.set_mode(size)


def mainMenu():

    print ("This is where the main menu will run")

def game():

    ##FPS management
    fps = 60
    loop_delta = 1./fps
    current_time = target_time = time.clock()

    #Player declaration
    playerImage = "square.png"
    
    player1 = player(0,0,playerImage,screen)
    player1.move((screenWidth/2)-(player1.width/2), (screenHeight/2)-(player1.height/2))


    #Platform for testing

    plat = gamePlatform(100,200,2,playerImage,playerImage,playerImage,screen)


    while True:

        #Set current and previous time for FPS
        #All code except for the display flip should be between
        #the two fps management snippets
        previous_time, current_time = current_time, time.clock()

        #Pygame event management
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        #Player Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] :
            print()
        if keys[pygame.K_a] :
            print()
        if keys[pygame.K_w] :
            print()
        if keys[pygame.K_s] :
            print()
        if keys[pygame.K_SPACE]:
            print()
        

        #Draw section
        screen.fill((0,0,0))
        player1.refresh()
        plat.refresh()

        #FPS management
        target_time += loop_delta
        sleep_time = target_time - time.clock()
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)
        

        pygame.display.flip()

game()
