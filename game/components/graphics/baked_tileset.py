import pygame

from game.ecs import Component
from game.utils.image_cache import get_image
from game.utils.constants import PPU
from ..graphics import Sprite, Surface

class BakedTileset(Component):
  def __init__(self, tileset):
    super().__init__()
    self.require(Sprite) #require sprite to get surface/position/rect
    self.tileset = tileset

  def start(self):
    self.surface = self.get_component(Surface)
    self.surface.set_surface(pygame.Surface((self.tileset.width * PPU, self.tileset.height * PPU)))

    for x, y, tile in self.tileset.itertiles():
      if tile.image_path is not None:
        image = get_image(tile.image_path)
        self.bake(image, x, y)

  def bake(self, image, x, y):
    self.surface.surface.blit(image, (x * PPU, y * PPU))
