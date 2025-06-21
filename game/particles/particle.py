import pygame
from pygame.math import Vector2

from game.constants import TILE_SIZE, DT
from game.utils.image_cache import get_image

#TODO: tintable particles
#TODO: homing particles
#TODO: particle swirls (circle around, swirl out, etc)
#TODO: scale particles
#TODO: rotate particles
#TODO: friction
#TODO: fading

class Particle(pygame.sprite.Sprite):
  def __init__(self, path, pos, vel=Vector2(0, 0), life=1):
    super().__init__()
    self.image = get_image(path)

    self.pos = pos
    self.vel = vel
    self.life = life
    #TODO: do particles actually need a rect? just use position
    self.rect = pygame.Rect(0, 0, 0, 0)

  def update(self):
    self.pos = self.pos + self.vel * DT
    self.life -= DT
    if self.life <= 0:
      self.kill()

  def draw(self, renderer):
    #TODO: apply offset?
    pos = self.pos * TILE_SIZE
    if offset is not None:
      pos -= offset
    self.rect.center = pos
    #TODO: may need to fix this since rendering refactor
    renderer.draw(self.image, self.rect.center)
