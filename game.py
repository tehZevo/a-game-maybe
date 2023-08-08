import pygame, sys
from pygame.math import Vector2
from save_data import SaveData

from utils.constants import PPU

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    #TODO: store a party (player game/"save" data) so player data can be repopulated on the new floor

    #TODO: make setup_world function?
    self.world = floor_transition(DFSGenerator())
    self.next_world = None
    self.init_world()

  def init_world(self, save_data=None):
    #find player (TODO: create new players and load save data)
    self.player = self.world.find(Player)[0]
    #store reference to game as an entity
    self.world.create_entity([GameMaster(self)])
    #add particle system
    self.particle_system = self.world.create_entity([ParticleSystem()])
    #create camera that targets player
    self.camera = self.world.create_entity([
      Position(self.player.get_component(Position).pos),
      Camera(target=self.player)
    ])

    #apply save data
    if save_data is not None:
      save_data.apply(self.world)

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

        #control player
        keys = pygame.key.get_pressed()
        self.player.get_component(Player).handle_keys(keys)

        #update world
        self.world.update()

        #render
        camera_pos = self.camera.get_component(Position).pos
        camera_offset = Vector2(*(camera_pos * PPU).tolist()) - Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.screen.fill((0, 0, 0))
        for e in self.world.entities:
          sprite = e.get_component(Sprite)
          if sprite is not None:
            sprite.draw(self.screen, camera_offset)

        self.particle_system.get_component(ParticleSystem).draw(self.screen, camera_offset)

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

        pygame.display.flip()

      #swap worlds, create new player (TODO: use generator spawn method? idk)
      save_data = SaveData(self.world)
      self.world = self.next_world
      self.init_world(save_data)
      self.next_world = None

from components.actor.player import Player
from components.graphics.sprite import Sprite
from components.graphics.camera import Camera
from components.physics.position import Position
from components.particles.particle_system import ParticleSystem
from components.core.game_master import GameMaster
from ecs import Entity, World
from floor_generators import TestFloor, DFSGenerator
from utils.constants import FPS
from utils.vector import Vector
from utils.floor_transition import floor_transition
