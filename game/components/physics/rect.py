import pygame

from ecs import Component
from components.physics.position import Position
from utils.constants import PHYS_SCALE

class Rect(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    #NOTE: scaling for collisions
    self.rect = pygame.Rect(0, 0, PHYS_SCALE, PHYS_SCALE)

  def set_rect(self, rect):
    self.rect = rect
    self.update()

  def start(self):
    self.pos = self.get_component(Position)
    self.update()

  def update(self):
    #keep self in sync with position
    #NOTE: scaling for collisions
    #self.rect.center = (self.pos.pos * PHYS_SCALE).tolist()
    self.rect.left = self.pos.pos.x * PHYS_SCALE
    self.rect.top = self.pos.pos.y * PHYS_SCALE
