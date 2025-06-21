import time
import asyncio
import sys
from collections import defaultdict

import pygame

from game.ecs import World
import game.components as C
from game.utils.constants import FPS, TILE_SIZE, DT
import game.networking.events as E
from game.networking.commands import Sync, Ping
from game.utils import Vector

#TODO: move to constants?
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
RENDER_WIDTH = TILE_SIZE * SCREEN_WIDTH_TILES
RENDER_HEIGHT = TILE_SIZE * SCREEN_HEIGHT_TILES

async def annoy_server(client):
  while True:
    client.send(Ping(time.time()))
    await asyncio.sleep(1)

#TODO: dont like this.. have to wait for client to connect...
class ClientConnectHandler:
  def __init__(self):
    pass
  
  def handle_connect(self, client):
    asyncio.create_task(annoy_server(client))
    client.send(Sync())

#TODO: allow setting url via ClientType class or something
class ClientGame:
  def __init__(self, client, scale_res=1):
    pygame.init()
    self.scale_res = scale_res
    screen_width = self.scale_res * RENDER_WIDTH
    screen_height = self.scale_res * RENDER_HEIGHT
    self.screen = pygame.display.set_mode((screen_width, screen_height))
    self.clock = pygame.time.Clock()
    
    pygame.display.set_caption("Game")
    #TODO: move to fps counter ui component...
    self.frames = 0
    self.one_second = 0
    self.last_frame_time = time.time()

    self.client = client
    self.client.setup_handlers(
      connect_handlers=[ClientConnectHandler()],
      event_handlers=[
        E.PlayerAssignedHandler(),
        E.TilesetUpdatedHandler(),
        E.ChunkLoadedHandler(),
        E.ChunkUnloadedHandler(),
        E.EntitySpawnedHandler(),
        E.PositionUpdatedHandler(),
        E.VelocityUpdatedHandler(),
        E.SpriteChangedHandler(),
        E.IconChangedHandler(),
        E.EmitterUpdatedHandler(),
        E.EntityDespawnedHandler(),
        E.MobUpdatedHandler(),
        E.StatsUpdatedHandler(),
        E.EquipsUpdatedHandler(),
        E.WorldClosedHandler(self),
        E.WorldOpenedHandler(),
        E.PongHandler(),
        E.BuffsUpdatedHandler(),
      ]
    )

    #create ui world and manager
    self.ui_world = World()
    self.hud = self.ui_world.create_entity([C.HUD()])
    self.ui_renderer = self.ui_world.create_entity([C.Renderer(RENDER_WIDTH, RENDER_HEIGHT)])

    self.world = World()
    self.next_world = None
    self.init_world()

  def init_world(self):
    #setup client world
    self.world.create_entity([C.GameMaster(self, None)]) #NOTE: we'll set mapdef when we get it from the server
    self.camera = self.world.create_entity([C.Camera()])
    self.renderer = self.world.create_entity([C.WorldRenderer(RENDER_WIDTH, RENDER_HEIGHT, self.camera)])
    self.world.create_entity([C.TileRendering()])
    self.world.create_entity([C.TilePhysics()])
    self.particle_system = self.world.create_entity([C.ParticleSystem()])
    
    #TODO: create Client as property of ClientGame and pass to ClientManager?
    client_manager = C.ClientManager()
    #TODO: remove binding if possible
    client_manager.client = self.client
    self.client.client_manager = client_manager
    self.world.create_entity([client_manager])

    #set hud world and player
    hud_comp = self.hud.get_component(C.HUD)
    hud_comp.game_world = self.world

  def transition(self):
    self.next_world = World()

  async def run(self):
    while True:
      #loop until we have a world to transition to
      while self.next_world is None:
        self.client.handle_events()

        #TODO: move to util function? (make sure to convert events to list first)
        pressed = defaultdict(lambda: False)
        released = defaultdict(lambda: False)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            pressed[event.key] = True
          if event.type == pygame.KEYUP:
            released[event.key] = True
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #control player
        held = pygame.key.get_pressed()
        player_controller = self.world.find_component(C.PlayerController)
        if player_controller is not None:
          player_controller.handle_keys(pressed, held, released)

        #update world
        self.world.update()

        #render
        self.screen.fill((0, 0, 0))
        self.renderer.get_component(C.Renderer).render(self.screen)

        #draw particles
        #TODO: reenable when i fix particle lag
        # camera_pos = self.camera.get_component(C.Position).pos
        # camera_offset = (camera_pos * TILE_SIZE) - Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        # self.particle_system.get_component(C.ParticleSystem).draw(self.screen, camera_offset)

        #draw UI
        self.ui_world.update()
        self.ui_renderer.get_component(C.Renderer).render(self.screen)

        #doing both this and clock.tick makes game run as expected, because of course it does
        self.clock.tick(FPS) #limit fps TODO: remove and decouple
        pygame.display.flip()

        self.frames += 1
        self.one_second += time.time() - self.last_frame_time
        self.last_frame_time = time.time()
        if self.one_second >= 1:
          print("[Client] FPS:", self.frames / self.one_second)
          self.one_second = 0
          self.frames = 0

        await asyncio.sleep(0)

      self.world = self.next_world
      self.init_world()
      self.next_world = None
