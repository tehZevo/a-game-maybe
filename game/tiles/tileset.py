from dataclasses import dataclass
from itertools import product
from typing import List

from . import Tile

#TODO: combine tilesets (ie draw one tileset onto another)
#TODO: somehow compress tileset for transfer.. png file?
@dataclass
class Tileset:
  width: int
  height: int
  tiles: List[List[Tile]]

  def __init__(self, width, height, tiles=None):
    super().__init__()
    self.width = width
    self.height = height
    self.tiles = [[None for _ in range(width)] for _ in range(height)] if tiles is None else tiles

  def set_tile(self, x, y, tile):
    self.tiles[y][x] = tile

  def get_tile(self, x, y):
    return self.tiles[y][x]

  def itertiles(self):
    return ((x, y, self.get_tile(x, y)) for x in range(self.width) for y in range(self.height) if self.get_tile(x, y) is not None)
