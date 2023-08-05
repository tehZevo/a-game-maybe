import pygame

from ecs import Component
from components import Position, Physics, Sprite

class Player(Component):
  def __init__(self):
    super().__init__()
    self.require(Physics)
    self.require(Sprite)

  def handle_keys(self, keys):
    phys = self.get_component(Physics)
    fx, fy = 0, 0

    if keys[pygame.K_LEFT]:
      fx -= 1
    if keys[pygame.K_RIGHT]:
      fx += 1
    if keys[pygame.K_UP]:
      fy -= 1
    if keys[pygame.K_DOWN]:
      fy += 1

    #TODO: normalize and use a MOVE_SPEED
    phys.apply_force(fx, fy)
