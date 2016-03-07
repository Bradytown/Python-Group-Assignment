
class entity():

    def __init__(self, x, y, image, screen):

        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
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

        moveRect(dx,dy)
        self.x+=dx
        self.y+=dy

    def refresh(self):
        self.screen.blit(self.image, (self.x,self.y))
