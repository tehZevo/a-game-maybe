import pygame

from constants import PPU
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

  def draw(self, screen):
    #TODO: update rect position elsewhere..
    pos = self.entity.get_component(Position)
    self.sprite.rect.center = pos.get_pos()
    screen.blit(self.sprite.surf, self.sprite.rect.center)
