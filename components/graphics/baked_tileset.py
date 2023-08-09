import pygame
from pygame.math import Vector2

from utils.constants import PPU, PIXEL_SCALE
from ecs import Component
from components.physics.position import Position
from utils.image_cache import get_image

#TODO: dunno where this belongs
class BakedTileset(Component):
  def __init__(self, tileset):
    super().__init__()
    self.require(Position)
    self.tileset = tileset
    self.surface = pygame.Surface((self.tileset.width * PPU, self.tileset.height * PPU))
    # self.surface.fill((255, 255, 255))

  def start(self):
    #TODO: use itertiles :)
    for x, y, tile in self.tileset.itertiles():
      if tile.solid:
        #TODO: create sprite? rect? something for collision?
        pass
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
