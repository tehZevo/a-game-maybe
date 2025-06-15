import pygame

from game.ecs import Component
import game.components as C
from game.utils.constants import TILE_SIZE
from game.utils import Vector

#TODO: split into "screen renderer" and "world renderer" (world renderer sorts by y)
#draws drawables
class Renderer(Component):
  def __init__(self, width, height):
    super().__init__()
    self.width = width
    self.height = height
    self.surface = pygame.Surface((width, height), flags=pygame.SRCALPHA)
    self.y_up = False #TODO: use
    self.sort_buffer = [] #TODO: use
  
  #TODO: rather than drawing directly to the screen, have drawables provide a list of surfaces to draw and at what positions, then have the renderer sort them
  #def renderer.draw(surface, x, y, alpha)
  def render(self, screen):
    self.surface.fill((0, 0, 0, 0))
    #TODO: set camera instead of just finding first
    #TODO: also this is expensive
    cameras = self.entity.world.find(C.Camera)
    if len(cameras) > 0:
      camera_pos = cameras[0].get_component(C.Position).pos
      camera_offset = (camera_pos * TILE_SIZE) - Vector(self.width / 2, self.height / 2)
    else:
      camera_offset = Vector()

    for drawable in self.entity.world.find_components(C.Drawable):
      drawable.draw(self.surface, -camera_offset)
    
    #scale and draw to screen
    scaled = pygame.transform.scale(self.surface, screen.get_size())
    screen.blit(scaled, (0, 0))
