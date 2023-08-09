from itertools import product

#TODO: combine tilesets (ie draw one tileset onto another)
class Tileset:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.tiles = [[None for _ in range(width)] for _ in range(height)]

  def set_tile(self, x, y, tile):
    self.tiles[y][x] = tile

  def get_tile(self, x, y):
    return self.tiles[y][x]

  def itertiles(self):
    return ((x, y, self.get_tile(x, y)) for x in range(self.width) for y in range(self.height) if self.get_tile(x, y) is not None)
