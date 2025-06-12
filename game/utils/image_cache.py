import pygame

cache = {}

def get_image(path):
  if path not in cache:
    img = pygame.image.load(path).convert_alpha()
    cache[path] = img

  return cache[path]
