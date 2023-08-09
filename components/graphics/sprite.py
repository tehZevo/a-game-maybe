import pygame
from pygame.math import Vector2

from utils.constants import PPU, PIXEL_SCALE
from ecs import Component
from components.physics.position import Position
from components.graphics.surface import Surface
from utils.image_cache import get_image, EMPTY_SURFACE

class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.require(Surface)

  def start(self):
    self.surface = self.get_component(Surface)
    self.rect = self.surface.surface.get_rect()

  def update(self):
    pos = self.entity.get_component(Position).pos
    self.rect.center = [e * PPU for e in pos.tolist()]

  #TODO: rename to set_image and update surface
  def set_sprite(self, path):
    self.surface.set_surface(get_image(path))
    self.rect = self.surface.surface.get_rect()
