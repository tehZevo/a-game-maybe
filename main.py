import pygame, sys

from ecs import Entity, World
from components import Player, Sprite

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

world = World()

player = Entity()
player.add_component(Player())
print(player.components)

world.add_entity(player)

pygame.display.set_caption("Hello World")
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys = pygame.key.get_pressed()
  player.get_component(Player).handle_keys(keys)

  world.update()

  screen.fill((0, 0, 0))

  sprite = player.get_component(Sprite)
  if sprite is not None:
    sprite.draw(screen)

  clock.tick(60) #limit fps TODO: remove

  pygame.display.flip()
