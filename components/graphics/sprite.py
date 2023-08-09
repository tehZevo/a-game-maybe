import pygame

from ecs import Component
from components.physics.position import Position
from components.graphics.surface import Surface
from utils.image_cache import get_image

class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.require(Surface)

  #TODO: rename to set_image and update surface
  def set_sprite(self, path):
    self.get_component(Surface).set_surface(get_image(path))
