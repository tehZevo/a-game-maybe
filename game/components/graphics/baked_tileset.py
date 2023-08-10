import pygame

from game.ecs import Component
from game.utils.image_cache import get_image
from game.utils.constants import PPU, PHYS_SCALE
from ..graphics import Sprite, Surface, Renderer

#TODO: dunno where this belongs, probably in core or tiles if this creates collision rects
class BakedTileset(Component):
  def __init__(self, tileset):
    super().__init__()
    self.require(Sprite) #require sprite to get surface/position/rect
    self.tileset = tileset
    self.rects = [] #list of rects to collide against for solid tiles

  def start(self):
    self.surface = self.get_component(Surface)
    self.surface.set_surface(pygame.Surface((self.tileset.width * PPU, self.tileset.height * PPU)))

    for x, y, tile in self.tileset.itertiles():
      if tile.solid:
        #NOTE: scaled for collision
        self.rects.append(pygame.Rect(x * PHYS_SCALE, y * PHYS_SCALE, PHYS_SCALE, PHYS_SCALE))
      if tile.image_path is not None:
        image = get_image(tile.image_path)
        self.bake(image, x, y)

  # def update(self):
  #   #debug rects
  #   screen = self.entity.world.find_components(Renderer)[0].screen
  #   for rect in self.rects:
  #     pygame.draw.rect(screen, (255, 0, 0), rect)
  #
  #   pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(1, 1, 1, 1))
  #   pygame.display.flip()

  def bake(self, image, x, y):
    self.surface.surface.blit(image, (x * PPU, y * PPU))
