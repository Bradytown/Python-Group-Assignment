import pygame
from pygame.locals import *
pygame.init()

class mouseCursor(pygame.sprite.DirtySprite):

    def __init__(self, x, y, image):

        pygame.sprite.DirtySprite.__init__(self)

        self.image = image

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        self.dirty = 2

    def resize(self,x,y):
        self.image = pygame.transform.scale(self.image,(x,y))
        self.rect = self.image.get_rect()

    def update(self):

        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.rect.x -= self.rect.width/2
        self.rect.y -= self.rect.height/2
        
