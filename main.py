import pygame, sys

from ecs import Entity, World
from components import Player, Sprite, DungeonFloor
from floor_generators import TestFloor
from utils.constants import FPS
from utils.vector import Vector
from utils.floor_transition import floor_transition

#TODO: use movespeed from stats

#TODO: persist player data across floors

#TODO: gold, health, mana drops: walk over them to pick them up

#TODO: maybe distinction between world sprite and ui sprite

#TODO: skill idea: "ally bomb" (or something like that): damage enemies nearby allies (target allies, then target enemies)

#TODO: make targets have a filter type: "enemies" or "allies" or "self"? idk

#TODO: distance based delay effect (delay in seconds per unit)
#TODO: ranged attacks will feel nicer with a bit of delay (think magic claw from maple story)

#TODO: camera
#TODO: concept of "teams" so player skill effects automatically target enemies (and vice versa)

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

player = Entity()
player.add_component(Player())

world = floor_transition(player, TestFloor())

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
