#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Scene.py

import sys, pygame, graphic, Director

class Scene:
	def __init__(self, director):
		self.director = director
		
	def onUpdate(self):
		raise NotImplemented("No implementado")
	def onEvent(self):
		raise NotImplemented("No implementado")
	def onDraw(self, screen):
		raise NotImplemented("No implementado")
