#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


import pygame, sys, config, MenuScene, PlayScene

class director:
	def __init__(self):
		self.screen = pygame.display.set_mode((config.width, config.height))
		pygame.display.set_caption("Pykanoid")
		self.scene = None
		self.quit_flag = False
		self.clock = pygame.time.Clock()
	
	def loop(self):
		while not self.quit_flag:
			time = self.clock.tick(60)
			for eventos in pygame.event.get():
				if eventos.type == pygame.QUIT:
					sys.exit(0)
			self.scene.onEvent(time)
			self.scene.onUpdate()
			self.scene.onDraw(self.screen)
			pygame.display.flip()
			
		pygame.quit()
	def changeScene(self, scene):
		self.scene = scene
	
	def quit(self):
		self.quit_flag = True
		
