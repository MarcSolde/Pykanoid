#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame, sys

def load_image(filename, transparent=False):
	try: image = pygame.image.load(filename)
	except pygame.error as message:
		raise SystemExit (message)
	image = image.convert()
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image
	
def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font("DroidSans.ttf", 25)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect	
	
