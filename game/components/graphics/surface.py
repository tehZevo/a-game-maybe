from game.ecs import Component
from game.utils.image_cache import EMPTY_SURFACE

class Surface(Component):
  def __init__(self):
    super().__init__()
    self.surface = EMPTY_SURFACE

  def set_surface(self, surface):
    self.surface = surface
