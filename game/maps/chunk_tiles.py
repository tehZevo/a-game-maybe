import math
from collections import defaultdict

from game.tiles import Tileset
from game.constants import CHUNK_SIZE

def chunk_tiles(tiles):
  chunks = defaultdict(lambda: Tileset(CHUNK_SIZE, CHUNK_SIZE))

  for (tx, ty), tile in tiles.items():
    cx, cy = math.floor(tx / 16), math.floor(ty / 16)
    chunk = chunks[(cx, cy)]
    local_x = tx - cx * CHUNK_SIZE
    local_y = ty - cy * CHUNK_SIZE
    chunk.set_tile(local_x, local_y, tile)
  
  return chunks