import pygame

from game.ecs import Component
import game.components as C
from . import Surface
from game.utils.image_cache import get_image

from ..networking.networkable import Networkable

class Sprite(Component, Networkable):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Position, Surface)
    self.path = path

  def start(self):
    if self.path is not None:
      self.set_sprite(self.path)

  def melt(self):
    return {
      "path": self.path
    }

  #TODO: rename to set_image and update surface
  def set_sprite(self, path):
    self.path = path

    #TODO: HACK: determine if we are on the client, and if not, do nothing!
    from ..networking import ClientManager
    if not self.entity.world.find_component(ClientManager):
      return

    self.get_component(Surface).set_surface(get_image(path))
