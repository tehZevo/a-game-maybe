import math
from collections import defaultdict
import itertools

import pygame

from game.ecs import Component
from game.utils.constants import PHYS_SCALE, CHUNK_SIZE

#NOTE: rects are in world space to make physics calculations simpler to understand
def build_rects(chunks):
  chunk_rects = defaultdict(list)
  for (cx, cy), chunk in chunks.items():
    for tx, ty, tile in chunk.itertiles():
      if not tile.solid:
        continue

      world_x = cx * CHUNK_SIZE + tx
      world_y = cy * CHUNK_SIZE + ty
      #TODO: greedy merging
      chunk_rects[(cx, cy)].append(pygame.Rect(world_x * PHYS_SCALE, world_y * PHYS_SCALE, PHYS_SCALE, PHYS_SCALE))
  return chunk_rects

class TilePhysics(Component):
  def __init__(self, chunks):
    super().__init__()
    self.chunk_rects = build_rects(chunks)
  
  #return 9 chunks in neighborhood of pos
  #TODO: cache these for each (pos / CHUNK_SIZE) chunk
  # (takes 9x memory but prevents having to regenerate rect list)
  def get_rects_for_pos(self, pos):
    center_cx = math.floor(pos.x / CHUNK_SIZE)
    center_cy = math.floor(pos.y / CHUNK_SIZE)
    rects = []
    for (offset_cx, offset_cy) in itertools.product([-1, 0, 1], [-1, 0, 1]):
      cx = center_cx + offset_cx
      cy = center_cy + offset_cy
      if (cx, cy) in self.chunk_rects:
        rects += self.chunk_rects[(cx, cy)]
    return rects