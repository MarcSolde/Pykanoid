import pygame, graphic,config

class Button(pygame.sprite.Sprite):
    def __int__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None

    def checkClick(self):
        if (pygame.mouse.get_pressed()[0]):
            return self.doThing()

    def doThing(self):
        p = pygame.mouse.get_pos()
        if self.rect.collidepoint(p[0],p[1]):
            return True
        return False

