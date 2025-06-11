import pygame

from ..physics import Position
from .ui_component import UIComponent

class Bar(UIComponent):
  def __init__(self):
    super().__init__()
    #TODO: use a rect as primary bounds and then calculate % based on value/max value?
    self.width = 256
    self.height = 16
    self.max_value = 100
    self.value = 75
    #TODO: color as a component?
    #TODO: auto determine bg color from color?
    self.color = (255, 0, 0)
    self.border_color = (0, 0, 0)
    self.bg_color = (255, 128, 128)

  def draw(self, screen, offset):
    pos = self.get_component(Position).pos
    #calculate rects
    bg_rect = pygame.Rect(pos.x, pos.y, self.width, self.height)
    value_rect = pygame.Rect(pos.x, pos.y, self.width * (self.value / self.max_value), self.height)
    #draw and fill rects
    #TODO: try border radius of 1?
    screen.fill(self.bg_color, bg_rect)
    screen.fill(self.color, value_rect)
    pygame.draw.rect(screen, self.border_color, bg_rect, width=1)
