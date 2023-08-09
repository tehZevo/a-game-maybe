import pygame
from pygame.math import Vector2

from utils.constants import PPU, PIXEL_SCALE
from ecs import Component
from components.physics.position import Position
from utils.image_cache import get_image

#TODO: dunno where this belongs
#TODO: manipulate position and auto expand canvas?
class Tileset(Component):
  def __init__(self, tiles):
    super().__init__()
    self.require(Position)
    self.tiles = tiles
    self.height = len(tiles)
    self.width = len(tiles[0])
    self.surface = pygame.Surface((self.width * PPU, self.height * PPU))
    self.surface.fill((255, 255, 255))

  def start(self):
    for y in range(self.height):
      for x in range(self.width):
        tile = self.tiles[x][y]
        if tile is None:
          continue
        if tile.solid:
          pass
          #TODO: create sprite? rect? something for collision?
        if tile.image_path is not None:
          image = get_image(tile.image_path)
          self.bake(image, x, y)

  def bake(self, image, x, y):
    self.surface.blit(image, (x * PPU, y * PPU))

  def draw(self, screen, offset=None):
    pos = self.entity.get_component(Position).pos
    pos = [e * PPU for e in pos.tolist()]

    if offset is not None:
      pos = pos - offset
    screen.blit(self.surface, pos)
