import pygame, sys
from pygame.math import Vector2

from utils.constants import PPU

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    #TODO: store a party (player game/"save" data) so player data can be repopulated on the new floor

    #TODO: make setup_world function?
    self.world = floor_transition(TestFloor())
    self.next_world = None
    self.init_world()

  def init_world(self):
    self.player = self.world.find(Player)[0]
    self.world.create_entity([GameMaster(self)])
    self.camera = self.world.create_entity([Camera(target=self.player)])

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

        camera_pos = self.camera.get_component(Position).pos
        camera_offset = Vector2(*(camera_pos * PPU).tolist()) - Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for e in self.world.entities:
          sprite = e.get_component(Sprite)
          if sprite is not None:
            sprite.draw(self.screen, camera_offset)

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

        pygame.display.flip()

      #swap worlds, create new player (TODO: use generator spawn method? idk)
      self.world = self.next_world
      self.init_world()
      self.next_world = None

from components.player import Player
from components.sprite import Sprite
from components.game_master import GameMaster
from components.camera import Camera
from components.position import Position
from ecs import Entity, World
from floor_generators import TestFloor
from utils.constants import FPS
from utils.vector import Vector
from utils.floor_transition import floor_transition
