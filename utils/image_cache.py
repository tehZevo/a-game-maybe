import pygame

cache = {}

def get_image(path):
  if path not in cache:
    cache[path] = pygame.image.load(path).convert_alpha()

  return cache[path]
