import pygame

from .component import Component
from constants import PPU

class _Sprite(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((PPU, PPU))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

  #TODO: make set_pos function (or wait till we have position component)
  def move(self, dx, dy):
    x, y = self.rect.center
    self.rect.center = [x + dx, y + dy]

  def draw(self, screen):
    screen.blit(self.surf, self.rect.center)

#TODO: make sprite require position component
class Sprite(Component):
  def __init__(self):
    super().__init__()
    self.sprite = _Sprite()

  def draw(self, screen):
    self.sprite.draw(screen)
