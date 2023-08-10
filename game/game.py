import pygame, sys
from pygame.math import Vector2

from game.ecs import World
from game.save_data import SaveData
from game.components.actor import Player
from game.components.graphics import Camera, Renderer
from game.components.physics import Position
from game.components.particles import ParticleSystem
from game.components.core import GameMaster
from game.components.ui import UIManager
from game.utils.constants import FPS, PPU
from game.utils.floor_transition import floor_transition
from game.floor_generators import TestFloor, DFSGenerator

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    #TODO: store a party (player game/"save" data) so player data can be repopulated on the new floor

    #create ui world and manager
    self.ui_world = World()
    self.ui_manager = self.ui_world.create_entity([UIManager()])

    #TODO: rename to game_world?
    self.world = floor_transition(DFSGenerator())
    # self.world = floor_transition(TestFloor())
    self.next_world = None
    self.init_world()

  def init_world(self, save_data=None):
    #find player (TODO: create new players and load save data)
    self.player = self.world.find(Player)[0]
    #store reference to game as an entity
    self.world.create_entity([GameMaster(self)])
    #create renderer
    self.renderer = self.world.create_entity([Renderer(self.screen)])
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

    #set ui manager world and player
    uim_comp = self.ui_manager.get_component(UIManager)
    uim_comp.game_world = self.world
    uim_comp.set_player(self.player)

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

        self.renderer.get_component(Renderer).render()

        #draw particles
        self.particle_system.get_component(ParticleSystem).draw(self.screen, camera_offset)

        #draw UI
        self.ui_world.update()
        self.ui_manager.get_component(UIManager).draw(self.screen)

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

        pygame.display.flip()

      #swap worlds, create new player (TODO: use generator spawn method? idk)
      save_data = SaveData(self.world)
      self.world = self.next_world
      self.init_world(save_data)
      self.next_world = None
