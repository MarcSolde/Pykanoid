#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  MenuScene.py

import Scene, graphic, config, pygame, playBttn, sys, HsBttn, PlayScene


class menuScene(Scene.Scene):
	def __init__(self, director):
		Scene.Scene.__init__(self, director)
		self.back = graphic.load_image(config.images+"menu.png")
		self.allThings = pygame.sprite.LayeredUpdates()
		self.Play = playBttn.PlayBttn()
		self.HS = HsBttn.HsBttn()
		self.allThings.add(self.Play, self.HS)

	def onUpdate(self):
		pass
	def onDraw(self, screen):
		screen.blit(self.back, (0,0))
		self.allThings.update()
		rects = self.allThings.draw(screen)
		pygame.display.update(rects)
	def onEvent(self, time):
		if (self.Play.checkClick()):
			self.director.changeScene(PlayScene.PlayScene(self.director))
		if (self.HS.checkClick()):
			print ("NOt Implementeds")
	
