import pygame, time, gameGlobals
from pygame.locals import *
from player import *
from gamePlatform import *


pygame.init()



screen = pygame.display.set_mode(gameGlobals.size)


def mainMenu():

    print ("This is where the main menu will run")

def game():



    #Functions

    def add(obj):
        allSpritesGroup.add(obj)
        allSpritesList.append(obj)


    def screenAssign():

        for i in range(0,len(allSpritesList)):

            if allSpritesList[i].onScreenCheck() and onScreenGroup.has(allSpritesList[i]) == False:
                onScreenGroup.add(allSpritesList[i])
                offScreenGroup.remove(allSpritesList[i])
            elif allSpritesList[i].onScreenCheck() == False and offScreenGroup.has(allSpritesList[i]) == False:
                print("Off Screen")
                offScreenGroup.add(allSpritesList[i])
                onScreenGroup.remove(allSpritesList[i])

                



    #Sprite Group Declarations

    allSpritesGroup = pygame.sprite.Group()
    onScreenGroup = pygame.sprite.Group()
    offScreenGroup = pygame.sprite.Group()

    #Sprite list

    allSpritesList = []

    ##FPS management
    fps = 60
    loop_delta = 1./fps
    current_time = target_time = time.clock()


    #Player declaration

    playerSpeed = 3
    
    playerImage = pygame.image.load("Characters\Guy with Gun.png")
    player1 = player(0,0,playerImage)
    player1.resize(gameGlobals.playerWidth,gameGlobals.playerHeight)

    add(player1)

    #Moving player to centre
    #xOrig and yOrig in globals
    
    player1.move(gameGlobals.xOrig, gameGlobals.yOrig)

    #Platforms

    platform4Image = pygame.image.load("Platforms & Walls\platform4.png")
    plat = gamePlatform(100,200,2,platform4Image)

    add(plat)

    backgroundImage = pygame.image.load("Backgrounds\City.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (gameGlobals.screenWidth, gameGlobals.screenHeight))
    

    screenAssign()
    
    
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
            player1.move(playerSpeed,0)
        if keys[pygame.K_a] :
            player1.move(-playerSpeed,0)
        if keys[pygame.K_SPACE]:
            print()
        

        #List Assignement

        #for i in range(0, len(offScreenList)):
            
        
        #Draw section
        screen.blit(backgroundImage,(0,0))

        allSpritesGroup.update()
        updateArea = allSpritesGroup.draw(screen)

        screenAssign()

        print(onScreenGroup.sprites())

        pygame.display.update()


        #FPS management
        target_time += loop_delta
        sleep_time = target_time - time.clock()
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)

        

game()
