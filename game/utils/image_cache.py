import pygame

from game.utils.constants import PIXEL_SCALE

cache = {}

def get_image(path):
  if path not in cache:
    #TODO: is it really best to scale here (no. do PPU/scaling calc in renderer)
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (img.get_width() * PIXEL_SCALE, img.get_height() * PIXEL_SCALE))
    cache[path] = img

  return cache[path]
