import pygame

from game.ecs import Component
from game.utils.constants import PPU, PHYS_SCALE

class TilesetPhysics(Component):
  def __init__(self, tileset):
    super().__init__()
    self.tileset = tileset
    #list of rects to collide against for solid tiles
    self.rects = []

  def start(self):
    for x, y, tile in self.tileset.itertiles():
      if tile.solid:
        #NOTE: scaled for collision
        #TODO: greedy merging
        self.rects.append(pygame.Rect(x * PHYS_SCALE, y * PHYS_SCALE, PHYS_SCALE, PHYS_SCALE))
