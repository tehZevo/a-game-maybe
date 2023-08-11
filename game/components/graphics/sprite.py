import pygame

from game.ecs import Component
from ..physics import Position
from . import Surface
from game.utils.image_cache import get_image

class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.require(Surface)

  #TODO: rename to set_image and update surface
  def set_sprite(self, path):
    from ..networking import ClientManager
    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    if not self.entity.world.find_component(ClientManager):
      return

    print(self.entity.components)
    self.get_component(Surface).set_surface(get_image(path))
