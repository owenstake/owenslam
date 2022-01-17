#!/usr/bin/python3.8
import time
import cv2
import pygame
import sdl2.ext
import numpy as np

import pygame
from pygame.locals import DOUBLEBUF


class Display():
    def __init__(self, w, h):
        sdl2.ext.init()

        self.W, self.H = w, h
        self.window = sdl2.ext.Window("twitch SLam", size=(self.W,self.H), position=(-500,-500))
        self.window.show()

    def paint(self, img):
        # paint
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)
        surf = sdl2.ext.pixels3d(self.window.get_surface()) 
        print(img.shape)
        print(surf.shape)
        # surf[:, :, 0:3] = img.swapaxes(0,1)
        surf[:, :, 0:3] = img.swapaxes(0,1)
        self.window.refresh()

class Display2D(object):
  def __init__(self, W, H):
    pygame.init()
    self.screen = pygame.display.set_mode((W, H), DOUBLEBUF)
    self.surface = pygame.Surface(self.screen.get_size()).convert()

  def paint(self, img):
    # junk
    for event in pygame.event.get():
      pass

    # draw
    #pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [2,1,0]])

    # RGB, not BGR (might have to switch in twitchslam)
    pygame.surfarray.blit_array(self.surface, img.swapaxes(0,1)[:, :, [0,1,2]])
    self.screen.blit(self.surface, (0,0))

    # blit
    pygame.display.flip()


