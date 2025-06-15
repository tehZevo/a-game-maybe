import pygame

from .renderer import Renderer
import game.components as C
from game.utils.constants import TILE_SIZE
from game.utils import Vector

#TODO: y-sort
#TODO: flip y
#TODO: scale positions by TILE_SIZE
#TODO: screen shake?
class WorldRenderer(Renderer):
  def __init__(self, width, height):
    super().__init__(width, height)
  
  def transform(self, call, camera_offset):
    surface, pos, area, alpha = call
    return [surface, pos * TILE_SIZE + camera_offset, area, alpha]

  def modify_draw_calls(self, calls):
    #TODO: find is expensive, set camera on world renderer instead
    cameras = self.entity.world.find(C.Camera)
    if len(cameras) > 0:
      camera_pos = cameras[0].get_component(C.Position).pos
      camera_offset = (-camera_pos * TILE_SIZE) + Vector(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector()

    return [self.transform(call, camera_offset) for call in calls]
