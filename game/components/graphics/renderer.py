import time
import math

import pygame

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
    self.draw_calls = []
  
  def gather_draw_calls(self):
    for drawable in self.entity.world.find_components(C.Drawable):
      drawable.draw(self)
  
  def draw(self, surface, pos, area=None, alpha=1):
    self.draw_calls.append((surface, pos, area, alpha))
  
  #NOTE: override me if you want to process calls before rendering
  def modify_draw_calls(self, calls):
    return calls

  def render(self, screen):
    t = time.time()
    self.gather_draw_calls()
    #TODO: copy is currently pretty negligible with 8x8 12x12 rooms,
    # may need to revisit removing .copy later
    self.draw_calls = self.modify_draw_calls(self.draw_calls.copy())

    self.surface.fill((0, 0, 0, 0))
    for (surface, pos, area, alpha) in self.draw_calls:
      #TODO: use alpha
      #TODO: do i need to reset this?
      alpha = 255 if alpha is None else math.floor(alpha * 255)
      surface.set_alpha(alpha)
      self.surface.blit(surface, (pos.x, pos.y), area)

    #scale and draw to screen
    scaled = pygame.transform.scale(self.surface, screen.get_size())
    screen.blit(scaled, (0, 0))
    
    self.draw_calls = []
    dt = time.time() - t
    print("render took", dt, "s")
