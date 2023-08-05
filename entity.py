import pygame

ENTITY_SIZE = 32

class Entity(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surf = pygame.Surface((ENTITY_SIZE, ENTITY_SIZE))
    self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

  def move(self, dx, dy):
    x, y = self.rect.center
    self.rect.center = [x + dx, y + dy]

  def draw(self, screen):
    screen.blit(self.surf, self.rect.center)
