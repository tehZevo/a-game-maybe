import pygame, sys

from entity import Entity
#TODO: reorg to from components import Sprite
from components.sprite import Sprite

pygame.init()
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

player = Entity()
player.add_component(Sprite())
print(player.components)

pygame.display.set_caption("Hello World")
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    player.move(-1, 0)
  if keys[pygame.K_RIGHT]:
    player.move(1, 0)
  if keys[pygame.K_UP]:
    player.move(0, -1)
  if keys[pygame.K_DOWN]:
    player.move(0, 1)

  screen.fill((0, 0, 0))

  sprite = player.get_component(Sprite)
  if sprite is not None:
    sprite.draw(screen)

  clock.tick(60) #limit fps TODO: remove

  pygame.display.flip()
