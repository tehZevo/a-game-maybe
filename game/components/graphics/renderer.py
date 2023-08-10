import pygame
from pygame.math import Vector2

from ecs import Component
from utils.constants import PPU
from components.graphics.camera import Camera
from components.graphics.surface import Surface
from components.graphics.sprite import Sprite
from components.physics.position import Position

#draws sprites
class Renderer(Component):
  def __init__(self, screen):
    super().__init__()
    self.screen = screen
    self.width, self.height = screen.get_size()

  def render(self):
    self.screen.fill((0, 0, 0))
    cameras = self.entity.world.find(Camera)
    self.camera = cameras[0] if len(cameras) > 0 else None
    camera_pos = self.camera.get_component(Position).pos
    camera_offset = Vector2(*(camera_pos * PPU).tolist()) - Vector2(self.width / 2, self.height / 2)

    for entity in self.entity.world.find(Sprite):
      surface = entity.get_component(Surface)
      pos = entity.get_component(Position).pos
      pos = Vector2(*(e * PPU for e in pos.tolist()))
      self.screen.blit(surface.surface, pos - camera_offset)
