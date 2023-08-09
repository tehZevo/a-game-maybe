import pygame
from utils.constants import PIXEL_SCALE, PPU

cache = {}

EMPTY_SURFACE = pygame.Surface((PPU, PPU))

def get_image(path):
  if path not in cache:
    #TODO: is it really best to scale here?
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (img.get_width() * PIXEL_SCALE, img.get_height() * PIXEL_SCALE))
    cache[path] = img

  return cache[path]
