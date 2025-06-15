import pygame

cache = {}

def get_image(path):
  if path not in cache:
    #TODO: see if .convert results in faster rendering than .convert_alpha
    # if so, we may need to add a param here or somehow determine that an image should be convert with alpha
    img = pygame.image.load(path).convert_alpha()
    cache[path] = img

  return cache[path]
