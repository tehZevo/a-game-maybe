import math

import pygame

from .renderer import Renderer
import game.components as C
from game.utils.constants import TILE_SIZE
from game.utils import Vector

#TODO: consider how i want items/monstes to render when next to player
def y_sort(call):
  surface, pos, area, _, _ = call
  # height = area[3] if area is not None else surface.get_size()[1]
  return math.ceil(call[1].y)
  # return math.ceil(pos.y + height / TILE_SIZE)

#TODO: y-sort
#TODO: flip y
#TODO: screen shake?
class WorldRenderer(Renderer):
  def __init__(self, width, height, camera):
    super().__init__(width, height)
    self.camera = camera
  
  def transform(self, call, camera_offset):
    surface, pos, area, tint, alpha = call
    return (surface, pos * TILE_SIZE + camera_offset, area, tint, alpha)

  def modify_draw_calls(self, calls):
    if self.camera is not None:
      camera_pos = self.camera.get_component(C.Position).pos
      camera_offset = (-camera_pos * TILE_SIZE) + Vector(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector()

    
    calls = sorted(calls, key=y_sort)
    return [self.transform(call, camera_offset) for call in calls]
