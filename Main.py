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

                
    def checkClass(obj):

        return obj.__class__.__name__


    #Sprite Group Declarations

    allSpritesGroup = pygame.sprite.Group()
    onScreenGroup = pygame.sprite.RenderUpdates()
    offScreenGroup = pygame.sprite.Group()

    #Sprite list

    allSpritesList = []
    bulletList = []

    ##FPS management
    fps = 60
    loop_delta = 1./fps
    current_time = target_time = time.clock()


    #Player declaration

    playerSpeed = 3

    bulletImage = pygame.image.load("Bullet & Sparks\Bullet.png")
    bulletImage = pygame.transform.scale(bulletImage,(10,8))
    
    playerImage = pygame.image.load("Characters\Guy with Gun.png")
    player1 = player(0,0,playerImage,bulletImage,(3,8))
    player1.resize(gameGlobals.playerWidth,gameGlobals.playerHeight)
    player1.gravity(True)

    add(player1)


    #z
    #Moving player to centre
    #xOrig and yOrig in globals
    
    player1.move(gameGlobals.xOrig, gameGlobals.yOrig)

    #Platforms

    platform4Image = pygame.image.load("Platforms & Walls\platform4.png")
    plat = gamePlatform(200,400,2,platform4Image)

    add(plat)

    backgroundImage = pygame.image.load("Backgrounds\City.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (gameGlobals.screenWidth, gameGlobals.screenHeight))
    
    screen.blit(backgroundImage,(0,0))

    screenAssign()
    
    pygame.display.update()

    
    while True:

        #Set current and previous time for FPS
        #All code should be between
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
            bulletList.append(player1.shoot())
            add(bulletList[len(bulletList)-1])


        #onScreen management


        for i in range(0,len(allSpritesList)):
            if onScreenGroup.has(allSpritesList[i]):
                #Put Collision stuff here

                check = checkClass(allSpritesList[i])

                if check == "gamePlatform":
                    
                    if pygame.sprite.collide_rect(player1, plat):
                        player1.fallSpeed = 0
                        

        
        #Draw section
        screen.blit(backgroundImage,(0,0))

        allSpritesGroup.update()
        updateArea = onScreenGroup.draw(screen)

        screenAssign()

        pygame.display.update(updateArea)


        #FPS management
        target_time += loop_delta
        sleep_time = target_time - time.clock()
        if sleep_time < 0:
            sleep_time = 0
        time.sleep(sleep_time)

        

game()
