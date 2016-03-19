import Scene, graphic, config, pygame, bola, bloque

class PlayScene(Scene.Scene):
    def __init__(self, director):
        Scene.Scene.__init__(self, director)
        self.back = graphic.load_image(config.images+"menu.png")
        #Pala = Pala()
        self.Bola = bola.Bola()
        self.Bloque = bloque.Bloque()
        self.allSprites = pygame.sprite.LayeredDirty((self.Bloque, self.Bola))
        #allSprites.clear(pygame.display.set_mode((config.width, config.height), self.back))

    def onUpdate(self):
        pass
    def onDraw(self, screen):
        screen.blit(self.back, (0,0))
        self.allSprites.update()
        rects = self.allSprites.draw(screen)
        pygame.display.update(rects)

    def onEvent(self, director, time):
        self.Bola.actualizar(time)
        self.Bloque.actualizar(self.Bola)
