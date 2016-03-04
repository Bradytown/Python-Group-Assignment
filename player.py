#Player Class File


class player():

    def __init__(self, image, Rect):

        #Sets Image
        self.image = pygame.image.load(image)

    def setRect(x,y,width,height):

        self.rect = pygame.Rect(x,y,width,height)
