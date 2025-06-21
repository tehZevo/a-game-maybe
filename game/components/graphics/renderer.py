import time
import math

import pygame

from game.ecs import Component
import game.components as C
from game.constants import TILE_SIZE
from game.utils import Vector

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
  
  def draw(self, surface, pos, area=None, tint=None, alpha=1, offset=None, flip_x=False):
    self.draw_calls.append((surface, pos, area, tint, alpha, offset, flip_x))
  
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
    blits = []
    for (surface, pos, area, tint, alpha, offset, flip_x) in self.draw_calls:
      #TODO: use image_utils?
      if tint is not None:
        surface = surface.copy()
        surface.fill(tint, special_flags=pygame.BLEND_MULT)

      alpha = 255 if alpha is None else math.floor(alpha * 255)
      surface.set_alpha(alpha)
      draw_pos = pos + (offset or Vector())
      if area is not None:
        surface = surface.subsurface(area)
      if flip_x:
        surface = pygame.transform.flip(surface, True, False)
      blits.append((surface, (draw_pos.x, draw_pos.y)))
    self.surface.blits(blits)

    #scaling is slow in pygbag rely on hardware scaling in browser
    #TODO: for now, just detecting if we need to scale. later: use renderer.surface in client?
    if screen.get_size() != self.surface.get_size():
      scaled = pygame.transform.scale(self.surface, screen.get_size())
      screen.blit(scaled, (0, 0))
    else:
      screen.blit(self.surface, (0, 0))
    
    self.draw_calls = []
    dt = time.time() - t
    # print("render took", dt, "s")
