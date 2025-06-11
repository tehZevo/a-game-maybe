import pygame
from pygame.math import Vector2

from game.ecs import Component
import game.components as C
from game.utils.constants import PPU

#TODO: do ppu/upscaling calc here
#draws drawables
class Renderer(Component):
  def __init__(self, screen):
    super().__init__()
    self.screen = screen
    self.width, self.height = screen.get_size()

  def render(self):
    cameras = self.entity.world.find(C.Camera)
    if len(cameras) > 0:
      camera_pos = cameras[0].get_component(C.Position).pos
      camera_offset = Vector2(*(camera_pos * PPU).tolist()) - Vector2(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector2()

    for drawable in self.entity.world.find_components(C.Drawable):
      drawable.draw(self.screen, -camera_offset)
