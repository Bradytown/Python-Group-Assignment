import pygame, gameGlobals
from pygame.locals import *
pygame.init()

class entity(pygame.sprite.DirtySprite):

    def __init__(self, x, y, image):


        pygame.sprite.DirtySprite.__init__(self)

        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()

        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        self.dirty = 2

    def move(self,dx,dy):

        self.x+=dx
        self.y+=dy

    def resize(self,x,y):
        self.image = pygame.transform.scale(self.image,(x,y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = self.image.get_rect()

    def update(self):
        
        self.rect.x = self.x - gameGlobals.playerX + gameGlobals.xOrig
        self.rect.y = self.y - gameGlobals.playerY + gameGlobals.yOrig

        
