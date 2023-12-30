import pygame

from game.ecs import Component
import game.components as C
from . import Surface
from game.utils.image_cache import get_image

class Sprite(Component):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Position, Surface)
    self.path = path

  def start(self):
    if self.path is not None:
      self.set_sprite(self.path)

  #TODO: rename to set_image and update surface
  def set_sprite(self, path):
    self.path = path

    for component in self.entity.components.values():
      if not isinstance(component, C.SpriteListener):
        continue
      component.on_sprite_changed(self)

    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    #TODO: maybe move this logic to sprite networking since its behavior is different on client and server
    from ..networking import ClientManager
    if not self.entity.world.find_component(ClientManager):
      return

    self.get_component(Surface).set_surface(get_image(path))
