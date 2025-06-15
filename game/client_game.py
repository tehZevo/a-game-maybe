import pygame, sys

from game.ecs import World
import game.components as C
from game.utils.constants import FPS, TILE_SIZE
from game.networking import Client
import game.networking.events as E
from game.networking.commands import Sync
from game.utils import Vector

SCALE_RES = 3
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
RENDER_WIDTH = TILE_SIZE * SCREEN_WIDTH_TILES
RENDER_HEIGHT = TILE_SIZE * SCREEN_HEIGHT_TILES
SCREEN_WIDTH = SCALE_RES * RENDER_WIDTH
SCREEN_HEIGHT = SCALE_RES * RENDER_HEIGHT

#TODO: dont like this.. have to wait for client to connect...
class ClientConnectHandler:
  def __init__(self):
    pass
  
  def handle_connect(self, client):
    client.send(Sync())

class ClientGame:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption("Game")

    self.client = Client(
      connect_handlers=[ClientConnectHandler()],
      event_handlers=[
        E.PlayerAssignedHandler(),
        E.TilesetUpdatedHandler(),
        E.EntitySpawnedHandler(),
        E.PositionUpdatedHandler(),
        E.SpriteChangedHandler(),
        E.IconChangedHandler(),
        E.EmitterUpdatedHandler(),
        E.EntityDespawnedHandler(),
        E.StatsUpdatedHandler(),
        E.EquipsUpdatedHandler(),
        E.WorldClosedHandler(self),
        E.WorldOpenedHandler(),
      ]
    )

    #create ui world and manager
    self.ui_world = World()
    self.hud = self.ui_world.create_entity([C.HUD()])
    self.ui_renderer = self.ui_world.create_entity([C.Renderer(RENDER_WIDTH, RENDER_HEIGHT)])

    self.world = World()
    self.next_world = None
    self.init_world()

    #TODO: move this back up once we havae the "spawnme" or whatever command
    self.client.connect()

  def init_world(self):
    #setup client world
    self.world.create_entity([C.GameMaster(self, None)]) #NOTE: we'll set mapdef when we get it from the server
    self.camera = self.world.create_entity([C.Camera()])
    self.renderer = self.world.create_entity([C.WorldRenderer(RENDER_WIDTH, RENDER_HEIGHT, self.camera)])
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
        player_controller = self.world.find_component(C.PlayerController)
        if player_controller is not None:
          player_controller.handle_keys(keys)

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

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

        pygame.display.flip()

      #TODO: handle server world transitions
      self.world = self.next_world
      self.init_world()
      self.next_world = None
