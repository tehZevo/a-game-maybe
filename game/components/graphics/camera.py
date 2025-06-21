from game.ecs import Component
from ..physics import Position
from game.utils import Vector
from game.constants import CAMERA_BOX_SIZE

def clamp_box(target, camera):
  return max(target - CAMERA_BOX_SIZE, min(camera, target + CAMERA_BOX_SIZE))

class Camera(Component):
  def __init__(self, target=None):
    super().__init__()
    self.require(Position)
    self.target = target

  def update(self):
    if self.target is None:
      return

    target_pos = self.target.get_component(Position).pos
    camera_pos = self.get_component(Position).pos
    x = clamp_box(target_pos.x, camera_pos.x)
    y = clamp_box(target_pos.y, camera_pos.y)
    camera_pos = Vector(x, y)
    self.get_component(Position).pos = camera_pos
