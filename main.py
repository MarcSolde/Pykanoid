#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import pygame, sys, Director, MenuScene

def main():
    dire = Director.director()
    escena = MenuScene.menuScene(dire)
    dire.changeScene(escena)
    dire.loop()
    

if __name__ == '__main__':
    pygame.init()
    main()
