import math
from collections import defaultdict
import itertools

import pygame

from game.ecs import Component
from game.utils.constants import PHYS_SCALE, CHUNK_SIZE

#NOTE: rects are in world space to make physics calculations simpler to understand
def build_rects(cx, cy, chunk):
  #TODO: would use __iter__ but it doesnt start at 0, 0
  solid_tiles = defaultdict(lambda: False)
  solid_tiles.update({(x, y): t.solid for x, y, t in chunk.__iter__()})
  
  rects = []
  for y in range(CHUNK_SIZE):
    for x in range(CHUNK_SIZE):
      if not solid_tiles[(x, y)]:
        continue
      w = 0
      while True:
        if not solid_tiles[(x+w, y)]:
          break
        w += 1
      h = 0
      while True:
        if not all([solid_tiles[(x+w2, y+h)] for w2 in range(w)]):
          break
        h += 1
      if w > 0 and h > 0:
        for x2 in range(w):
          for y2 in range(h):
            solid_tiles[(x + x2, y + y2)] = False
        rects.append((x, y, w, h))
  rects = [pygame.Rect((cx * CHUNK_SIZE + x) * PHYS_SCALE, (cy * CHUNK_SIZE + y) * PHYS_SCALE, w * PHYS_SCALE, h * PHYS_SCALE) for x, y, w, h in rects]
  return rects

class TilePhysics(Component):
  def __init__(self, chunks):
    super().__init__()
    self.chunk_rects = {(x, y): build_rects(x, y, c) for (x, y), c in chunks.items()}
  
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