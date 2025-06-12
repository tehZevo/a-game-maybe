import pygame
from pygame.math import Vector2

from game.ecs import Component
import game.components as C
from game.utils.constants import TILE_SIZE

#draws drawables
class Renderer(Component):
  def __init__(self, width, height):
    super().__init__()
    self.width = width
    self.height = height
    self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
  
  def render(self, screen):
    self.surface.fill((0, 0, 0, 0))
    #TODO: set camera instead of just finding first
    #TODO: also this is expensive
    cameras = self.entity.world.find(C.Camera)
    if len(cameras) > 0:
      camera_pos = cameras[0].get_component(C.Position).pos
      camera_offset = Vector2(*(camera_pos * TILE_SIZE).tolist()) - Vector2(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector2()

    for drawable in self.entity.world.find_components(C.Drawable):
      drawable.draw(self.surface, -camera_offset)
    
    #scale and draw to screen
    scaled = pygame.transform.scale(self.surface, screen.get_size())
    screen.blit(scaled, (0, 0))
