import pygame

from utils.constants import PPU
from ecs import Component
from components import Position

class _Sprite(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((PPU, PPU))
    self.surf.fill((255, 255, 255))
    #TODO: rect should be part of position? or make Rect a component that requires Position
    self.rect = self.surf.get_rect()

class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.require(Position)
    self.sprite = _Sprite()
    #TODO: store rect here? or make it part of position? or its own component?
    self.img = None

  def set_sprite(self, path):
    self.img = pygame.image.load(path)

  def draw(self, screen):
    #TODO: update rect position elsewhere..
    pos = self.entity.get_component(Position).pos
    self.sprite.rect.center = [e * PPU for e in pos.tolist()]
    screen.blit(self.sprite.surf, self.sprite.rect.center)
    if self.img is not None:
      screen.blit(self.img, self.sprite.rect.center)
