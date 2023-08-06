import pygame, sys

from ecs import Entity, World
from components import Player, Sprite, Enemy, Position, Spawner
from utils.constants import FPS
from utils import Vector

#TODO: gold, health, mana drops: walk over them to pick them up

#TODO: i think items should be game data...

#TODO: maybe distinction between world sprite and ui sprite

#TODO: fix circular import issues

#TODO: can i make skill effects components? or should they stay as some kind of game data?

#TODO: chain targets, either:
# create chain target types (given a target, find more nearby targets)
# or make all target types take a target implicitly (use skill position if no target)
# ACTUALLY: better yet, child skill effects should be initialized at their target's location so chaining is natural?
# do we need a way to omit the original target or? probably not..

#TODO: skill idea: "ally bomb" (or something like that): damage enemies nearby allies (target allies, then target enemies)

#TODO: make targets have a filter type: "enemies" or "allies" or "self"? idk

#TODO: distance based delay effect (delay in seconds per unit)
#TODO: ranged attacks will feel nicer with a bit of delay (think magic claw from maple story)

#TODO: camera
#TODO: concept of "teams" so player skill effects automatically target enemies (and vice versa)

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

world = World()

player = Entity()
player.add_component(Player())
print(player.components)
world.add_entity(player)

spawner = Entity()
spawner.add_component(Position(Vector(10, 10)))
spawner.add_component(Spawner(Enemy))
world.add_entity(spawner)

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

  for e in world.entities:
    sprite = e.get_component(Sprite)
    if sprite is not None:
      sprite.draw(screen)

  clock.tick(FPS) #limit fps TODO: remove and decouple

  pygame.display.flip()
