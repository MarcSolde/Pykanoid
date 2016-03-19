#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

import sys, pygame, graphic, config
from pygame.locals import *

class Bloque(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.image = graphic.load_image(config.images+"bloque.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = 100
		self.rect.centery = 100
		self.dirty = 2
		self.visible = 1
	
	def setCenterX(self,valueX):
		self.centerx = valueX

	def setCenterY(self, valueY):
		self.centery = valueY
	
	def actualizar(self, bola):
		if pygame.sprite.collide_rect(self, bola):
			self.dirty = 2
			self.visible = 0
			self.kill()
			#TODO: incluir random para powerUp drop
