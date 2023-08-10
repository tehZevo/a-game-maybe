from game.ecs import Component
from ..physics import Position

LERP_RATE = 0.05

class Camera(Component):
  def __init__(self, target=None):
    super().__init__()
    self.require(Position)
    self.target = target

  def update(self):
    if self.target is None:
      return

    #lerp towards target
    target_pos = self.target.get_component(Position).pos
    camera_pos = self.get_component(Position).pos
    camera_pos = camera_pos + (target_pos - camera_pos) * LERP_RATE
    self.get_component(Position).pos = camera_pos
