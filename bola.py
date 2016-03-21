import pygame, graphic, config

class Bola(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.image = graphic.load_image(config.images+"ball.png", True)
		self.rect = self.image.get_rect()
		self.rect.centerx = config.width/2
		self.rect.centery = config.height/2
		self.speed = [0.25, -0.25]
		self.dirty = 2

	def actualizar(self, time):
		self.rect.centerx+= self.speed[0] * time
		self.rect.centery+= self.speed[1] * time
		if self.rect.left <= 0 or self.rect.right >= config.width:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0]*time
		if self.rect.top <= 0 or self.rect.bottom >= config.height:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1]*time
		#if pygame.sprite.collide_rect(self, pala_jug):
		#	self.speed[0] = -self.speed[0]
		#	self.rect.centerx += self.speed[0]*time
