import pygame
from pygame.math import Vector2

from game.ecs import Component
from ..graphics import Camera, Surface, Sprite
from ..physics import Position
from game.utils.constants import PPU

#TODO: do ppu/upscaling calc here
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
