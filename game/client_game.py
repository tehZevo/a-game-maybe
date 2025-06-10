import pygame, sys
from pygame.math import Vector2

from game.ecs import World
from game.components.graphics import Camera, Renderer
from game.components.physics import Position
from game.components.particles import ParticleSystem
from game.components.core import GameMaster
from game.components.ui import UIManager
from game.components.networking import ClientManager
from game.components.core import PlayerController
from game.utils.constants import FPS, PPU

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class ClientGame:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    #create ui world and manager
    self.ui_world = World()
    self.ui_manager = self.ui_world.create_entity([UIManager()])

    self.world = World()
    #create client
    #TODO: create Client as property of ClientGame and pass to ClientManager?
    self.world.create_entity([
      ClientManager()
    ])
    self.next_world = None
    self.init_world()

  def init_world(self):
    #store reference to game as an entity
    self.world.create_entity([GameMaster(self)])
    #create renderer
    self.renderer = self.world.create_entity([Renderer(self.screen)])
    #add particle system
    self.particle_system = self.world.create_entity([ParticleSystem()])
    #create camera that targets player
    self.camera = self.world.create_entity([Camera()])

    #set ui manager world and player
    uim_comp = self.ui_manager.get_component(UIManager)
    uim_comp.game_world = self.world
    # uim_comp.set_player(self.player) #TODO: uimanager needs player eventually

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
        #TODO: need a find first function (and find first component)
        pc = self.world.find(PlayerController)
        if len(pc) > 0:
          pc = pc[0]
          pc.get_component(PlayerController).handle_keys(keys)

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

      #TODO: handle server world transitions
      self.world = self.next_world
      self.init_world()
      self.next_world = None
