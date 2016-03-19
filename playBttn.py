import pygame, button
from button import *

class PlayBttn(button.Button):
    def __init__(self):
        button.Button.__init__(self)
        self.image = graphic.load_image(config.images+"play.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = config.width/2
        self.rect.centery = 300

