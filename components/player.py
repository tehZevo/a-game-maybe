import pygame

from components import Component, Position, Sprite

class Player(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.require(Sprite)

  def handle_keys(self, keys):
    pos = self.get_component(Position)
    x, y = pos.get_pos()

    if keys[pygame.K_LEFT]:
      x -= 1
    if keys[pygame.K_RIGHT]:
      x += 1
    if keys[pygame.K_UP]:
      y -= 1
    if keys[pygame.K_DOWN]:
      y += 1

    pos.set_pos(x, y)
