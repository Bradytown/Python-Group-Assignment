#Player Class File


class player():

    def __init__(self, x, y, image, Rect, screen):


        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        setRect(Rect)
        self.screen.blit(self.image,(x,y))

    def setRect(Rect):

        self.rect = pygame.Rect(Rect)

    def moveRect(dx,dy)

        self.rect.move(dx,dy)

    def move(dx,dy):

        moveRect(dx,dy)
        self.x+=dx
        self.y+=dy

    def refresh():

        self.screen.blit(self.image, (self.x,self.y))
