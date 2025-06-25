import sys

import time
import asyncio

import pygame

from game.constants import FPS, TILE_SIZE, DT
import game.networking.events as E
import game.networking.commands as C

from game.states import ClientMainMenuState, ClientPlayState, ClientLobbyState
from game.networking import LocalServer, LocalClient, WebsocketClient, JSWSClient
from game.server_game import ServerGame
from game.client_config import ClientConfig
from game.client_mode import ClientMode
from game.client_room import ClientRoom
from game.utils import Keyboard

#TODO: end game state when world closes
#TODO: add world opened handler to lobby state or some kind of loading state

#TODO: move to constants?
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
FPS_MEASURE_SECONDS = 10

#TODO: ping again
async def annoy_server(client):
  while True:
    client.default_channel.send(C.Ping(time.time()))
    await asyncio.sleep(10)

class ClientGame:
  def __init__(self, mode, scale_res=1):
    pygame.init()
    self.mode = mode #TODO: switch client type based on this
    self.scale_res = scale_res
    self.render_width = TILE_SIZE * SCREEN_WIDTH_TILES
    self.render_height = TILE_SIZE * SCREEN_HEIGHT_TILES
    screen_width = self.scale_res * self.render_width
    screen_height = self.scale_res * self.render_height
    self.screen = pygame.display.set_mode((screen_width, screen_height))
    self.clock = pygame.time.Clock()
    self.room_channel = None
    self.config = ClientConfig(self.mode)
    self.config.load()
    self.config.save()
    self.auto_ready = False #TODO: spaghetti
    self.room = None

    pygame.display.set_caption("Game") #TODO: change
    #TODO: move to fps counter ui component?
    self.frames = 0
    self.fps_measure_time = time.time()

    self.client = None
    self.state = ClientMainMenuState(self)
  
  def setup_client_handlers(self, on_connect):
    self.client.setup_handlers(
      connect_handlers=[on_connect],
      event_handlers=[
        E.PongHandler(self),
        E.RoomJoinedHandler(self),
      ]
    )
  
  def handle_pygame_events(self):
    events = list(pygame.event.get())
    keyboard = Keyboard(events)
    quit = any([e.type == pygame.QUIT for e in events])
    
    return keyboard, quit

  def join_game(self, join_code):
    self.create_multiplayer_client()
    on_connect = lambda client: client.default_channel.send(C.JoinRoom(join_code))
    self.setup_client_handlers(on_connect)

    #TODO: store task for cancelling later? or can we just disconnect client to kill it?
    asyncio.create_task(self.client.connect())
  
  def create_game(self):
    self.create_multiplayer_client()
    on_connect = lambda client: client.default_channel.send(C.CreateRoom())
    self.setup_client_handlers(on_connect)

    #TODO: store task for cancelling later? or can we just disconnect client to kill it?
    asyncio.create_task(self.client.connect())

  def create_multiplayer_client(self):
    url = "ws://" + self.config.server_url
    if self.mode == ClientMode.DESKTOP:
      self.client = WebsocketClient(url)
    elif self.mode == ClientMode.WEB:
      self.client = JSWSClient(url)
    else:
      raise ValueError("Unable to create client for mode", self.mode)
  
  def play_offline(self):
    #TODO: idk how i feel about storing server here
    self.server = LocalServer()
    self.server_game = ServerGame(self.server)
    asyncio.create_task(self.server.start())
    asyncio.create_task(self.server_game.run())

    self.client = LocalClient()
    on_connect = lambda client: client.default_channel.send(C.CreateRoom())
    self.auto_ready = True
    self.setup_client_handlers(on_connect)
    
    asyncio.create_task(self.client.connect(self.server))
  
  def play_offline_dev(self):
    import game.data.maps as M
    #TODO: dedupe
    #TODO: idk how i feel about storing server here
    self.server = LocalServer()
    self.server_game = ServerGame(self.server)
    asyncio.create_task(self.server.start())
    asyncio.create_task(self.server_game.run())

    self.client = LocalClient()
    on_connect = lambda client: client.default_channel.send(C.CreateRoom(M.dev_map.id))
    self.auto_ready = True
    self.setup_client_handlers(on_connect)
    
    asyncio.create_task(self.client.connect(self.server))

  #TODO: split up logic (send HelloLobby and await LobbyUpdated)
  def setup_room_and_lobby(self, room_channel_id, lobby_channel_id, players, join_code):
    self.room_channel = self.client.add_channel(room_channel_id)
    self.room_channel.setup_handlers([
      E.WorldOpenedHandler(self),
      E.WorldClosedHandler(self),
      E.LobbyOpenedHandler(self),
    ])
    lobby_channel = self.client.add_channel(lobby_channel_id)
    self.room = ClientRoom()
    self.room.join_code = join_code
    self.room.players = players
    self.state = ClientLobbyState(self, lobby_channel, join_code, self.auto_ready)

  def on_world_closed(self):
    self.client.remove_channel(self.state.channel.id)
    # self.state = None
  
  #TODO: rename function
  def load_world(self, channel_id):
    channel = self.client.add_channel(channel_id)
    self.state = ClientPlayState(self, channel)
    
  async def run(self):
    while True:
      if self.client is not None:
        self.client.handle_events()
      if self.room_channel is not None:
        self.room_channel.handle_events()
      
      keyboard, quit = self.handle_pygame_events()
      if quit:
        pygame.quit()
        sys.exit()

      if self.state is not None:
        self.state.step(keyboard)

      #doing both this and clock.tick makes game run as expected, because of course it does
      self.clock.tick(FPS) #limit fps TODO: decouple rendering from physics
      pygame.display.flip()

      self.frames += 1
      if time.time() - self.fps_measure_time > FPS_MEASURE_SECONDS:
        print("[Client] FPS:", self.frames / FPS_MEASURE_SECONDS)
        self.frames = 0
        self.fps_measure_time = time.time()

      await asyncio.sleep(0)
