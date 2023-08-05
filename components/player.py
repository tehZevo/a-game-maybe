import pygame

from ecs import Component
from components import Position, Physics, Sprite
from utils import Vector

class Player(Component):
  def __init__(self):
    super().__init__()
    self.require(Physics)
    self.require(Sprite)

  def handle_keys(self, keys):
    phys = self.get_component(Physics)
    force = Vector(0, 0)

    if keys[pygame.K_LEFT]:
      force.x -= 1
    if keys[pygame.K_RIGHT]:
      force.x += 1
    if keys[pygame.K_UP]:
      force.y -= 1
    if keys[pygame.K_DOWN]:
      force.y += 1

    force = force.normalized()
    #TODO: normalize and use a MOVE_SPEED
    phys.apply_force(force.x, force.y)
