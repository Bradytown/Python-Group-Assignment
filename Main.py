import pygame, time, gameGlobals
from pygame.locals import *
from player import *
from gamePlatform import *
from mouseCursor import *
from enemy import *


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
                offScreenGroup.add(allSpritesList[i])
                onScreenGroup.remove(allSpritesList[i])

                
    def checkClass(obj):

        return obj.__class__.__name__


    def loadLevel(x):
        
        f =  open("Levels\level_"+ str(x) + ".txt","r")

        loadType = ""

        platformCoordinates = []
        wallCoordinates = []
        enemyCoordinates = []
        
        for inp in f:
            
            if inp == "Platforms\n":
                loadType = "platform"
                                
            elif inp == "Walls":
                loadType = "wall"

            elif inp == "Enemies":
                loadType = "enemy"

            elif inp != "\n":
                #coordinate parsing
                spaceInd = inp.find(" ")
                newLineInd = inp.find("\n")
                
                xlen = spaceInd

                xCoordinate = 0
                yCoordinate = 0

                for i in range(0, xlen):

                    if i != 0:
                        xCoordinate = xCoordinate*10
                    xCoordinate += int(inp[i])

                for i in range(spaceInd+1, newLineInd):

                    if i != 0:
                        yCoordinate = yCoordinate*10
                    yCoordinate += int(inp[i])

                if loadType == "platform":

                    platformCoordinates.append((xCoordinate,yCoordinate))
                    
                elif loadType == "wall":
                    
                    wallCoordinates.append((xCoordinate,yCoordinate))
                    
                elif loadType == "enemy":

                    enemyCoordinates.append((xCoordinate,yCoordinate))
                    

        for i in range(0, len(platformCoordinates)):
            platformList.append(gamePlatform(platformCoordinates[i][0],platformCoordinates[i][1],platform4Image))
            add(platformList[i])
        for i in range(0, len(wallCoordinates)):
            print("Implement walls")

        for i in range(0, len(enemyCoordinates)):
            enemyList.append(enemy(enemyCoordinates[i][0],enemyCoordinates[i][1],enemyImage))



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

    #mouse cursor

    cursorImage = pygame.image.load("Bullet & Sparks\crosshair.png")
    cursor = mouseCursor(0,0,cursorImage)
    cursor.resize(50,50)

    pygame.mouse.set_visible(False)

    allSpritesGroup.add(cursor)
    onScreenGroup.add(cursor)


    #z
    #Moving player to centre
    #xOrig and yOrig in globals
    
    player1.move(gameGlobals.xOrig, gameGlobals.yOrig)

    #Platforms

    platform4Image = pygame.image.load("Platforms & Walls\platform4.png")

##    plat = gamePlatform(200,400,platform4Image)
##
##    add(plat)

    backgroundImage = pygame.image.load("Backgrounds\City.png")
    backgroundImage = pygame.transform.scale(backgroundImage, (gameGlobals.screenWidth, gameGlobals.screenHeight))
    
    screen.blit(backgroundImage,(0,0))

    screenAssign()
    
    pygame.display.update()



#=============================================================================    
#=============================================================================
    
    loadLevel(1)


#=============================================================================
#============================================================================= 

    
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


        mousePos = mouseX, mouseY = pygame.mouse.get_pos()

        if (player1.direction == "left" and mouseX > player1.rect.x + player1.width) or (player1.direction == "right" and mouseX < player1.rect.x):
            player1.flip()
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player1.move(playerSpeed,0)
        if keys[pygame.K_a]:
            player1.move(-playerSpeed,0)
        if keys[pygame.K_SPACE]:
            bulletList.append(player1.shoot())
            add(bulletList[len(bulletList)-1])



        #onScreen management

        deleteList = []
        for i in range(0,len(allSpritesList)):
            if onScreenGroup.has(allSpritesList[i]):
                #Put Collision stuff here

                check = checkClass(allSpritesList[i])

                if check == "gamePlatform":

                    if pygame.sprite.collide_rect(player1, allSpritesList[i])and player1.y + 140 > plat.y:
                        player1.fallSpeed = 0
                        


        #Code to destroy collided bullet, enemies, etc.
        
        for i in range (0,len(deleteList)):
            del bullets[deleteList[i]-i]

        
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
