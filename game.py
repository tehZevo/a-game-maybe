import pygame, sys

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((640, 480))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    #TODO: store a party (player game/"save" data so player data can be repopulated on the new floor)

    #TODO: pass game instance to player?
    self.world = floor_transition(TestFloor())
    self.player = self.world.find(Player)[0]
    self.next_world = None

  def transition(self, world):
    self.next_world = world

  def run(self):
    while True:
      #loop until we have a world to transition to
      while self.next_world is None:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        self.player.get_component(Player).handle_keys(keys)

        self.world.update()

        self.screen.fill((0, 0, 0))

        for e in self.world.entities:
          sprite = e.get_component(Sprite)
          if sprite is not None:
            sprite.draw(self.screen)

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

        pygame.display.flip()

      #swap worlds, create new player (TODO: use generator spawn method? idk)
      self.world = self.next_world
      self.player = self.world.find(Player)[0]
      self.next_world = None

from components.player import Player
from components.sprite import Sprite
from ecs import Entity, World
from floor_generators import TestFloor
from utils.constants import FPS
from utils.vector import Vector
from utils.floor_transition import floor_transition
