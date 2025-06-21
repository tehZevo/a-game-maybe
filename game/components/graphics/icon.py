from pygame import Vector2

from game.ecs import Component
from .drawable import Drawable
import game.components as C
from game.utils.image_cache import get_image
from game.constants import TILE_SIZE

class Icon(Component, Drawable):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Position)
    self.image_path = path
    self.image = None
    self.pos = None

  def start(self):
    self.pos = self.get_component(C.Position)
    
    if self.image_path is not None:
      self.set_image(self.image_path)

  def set_image(self, path):
    if self.image_path == path:
      return

    self.image_path = path

    for component in self.entity.components.values():
      if not isinstance(component, C.IconListener):
        continue
      component.on_icon_changed(self)

    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    #TODO: maybe move this logic to icon networking since its behavior is different on client and server
    if not self.entity.world.find_component(C.ClientManager):
      return

    self.image = get_image(path)

  def draw(self, renderer):
    if self.image is not None:
      renderer.draw(self.image, self.pos.pos.copy())