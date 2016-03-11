import pygame
from pygame.locals import *
pygame.init()

class entity():

    def __init__(self, x, y, image, screen):

        self.x = x
        self.y = y
        self.image = image
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.setRect((self.x,self.y,self.height, self.width))
        self.screen = screen
        self.screen.blit(self.image,(x,y))

    def setRect(self, Rect):

        self.rect = pygame.Rect(Rect)

    def moveRect(self,dx,dy):

        self.rect.move(dx,dy)

    def move(self,dx,dy):

        self.moveRect(dx,dy)
        self.x+=dx
        self.y+=dy

    def resize(self,x,y):
        self.image = pygame.transform.scale(self.image,(x,y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def refresh(self):
        self.screen.blit(self.image, (self.x,self.y))

    
