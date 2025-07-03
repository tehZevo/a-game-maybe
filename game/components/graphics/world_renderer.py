import math
from collections import defaultdict
import itertools

import pygame

from .renderer import Renderer
import game.components as C
from game.constants import TILE_SIZE
from game.utils import Vector

#TODO: consider how i want items/monstes to render when next to player
#TODO: i might need a DrawCall class and WorldDrawCall to extend
# so we can set an offset that doesn't affect y sorting.. or specify a manual y sort value
def y_sort(call):
  surface, pos, area, _, _, offset, _ = call
  height = area[3] if area is not None else surface.get_size()[1]
  #second clause works but not sure why
  return (pos.y - height / TILE_SIZE, -offset.y if offset else 0)

#TODO: flip y
#TODO: screen shake?
class WorldRenderer(Renderer):
  def __init__(self, width, height, camera):
    super().__init__(width, height)
    self.camera = camera
  
  def transform(self, call, camera_offset):
    surface, pos, area, tint, alpha, offset, flip_x = call
    new_pos = pos * TILE_SIZE + camera_offset
    new_offset = offset and (offset * TILE_SIZE)
    return (surface, new_pos, area, tint, alpha, new_offset, flip_x)

  def modify_draw_calls(self, calls):
    if self.camera is not None:
      camera_pos = self.camera.get_component(C.Position).pos
      camera_offset = (-camera_pos * TILE_SIZE) + Vector(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector()
    
    calls = sorted(calls, key=y_sort)
    return [self.transform(call, camera_offset) for call in calls]
