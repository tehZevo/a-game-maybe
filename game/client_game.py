import sys
from enum import IntEnum
import time
import asyncio
from collections import defaultdict

import pygame

from game.constants import FPS, TILE_SIZE, DT
import game.networking.events as E
import game.networking.commands as C

from game.states import ClientMainMenuState, ClientPlayState, ClientLobbyState
from game.networking import LocalServer, LocalClient, WebsocketClient, JSWSClient
from game.server_game import ServerGame

ClientMode = IntEnum("ClientMode", ["DESKTOP", "WEB"])

#TODO: end game state when world closes
#TODO: add world opened handler to lobby state or some kind of loading state

#TODO: move to constants?
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
FPS_MEASURE_SECONDS = 10

async def annoy_server(client):
  while True:
    client.default_channel.send(C.Ping(time.time()))
    await asyncio.sleep(10)

#TODO: dont like this.. have to wait for client to connect...
class ClientConnectHandler:
  def __init__(self):
    pass
  
  def handle_connect(self, client):
    client.default_channel.send(C.CreateRoom())
    asyncio.create_task(annoy_server(client))

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

    pygame.display.set_caption("Game") #TODO: change
    #TODO: move to fps counter ui component?
    self.frames = 0
    self.fps_measure_time = time.time()

    self.client = None
    self.state = ClientMainMenuState(self)
  
  def create_multiplayer_client(self):
    #TODO: hardcoded url
    url = "ws://127.0.0.1:8765"
    if self.mode == ClientMode.DESKTOP:
      self.client = WebsocketClient(url)
    elif self.mode == ClientMode.WEB:
      self.client = JSWSClient(url)
    else:
      raise ValueError("Unable to create client for mode", self.mode)
    
    self.client.setup_handlers(
      connect_handlers=[ClientConnectHandler()],
      event_handlers=[
        E.PongHandler(self),
        E.RoomJoinedHandler(self),
      ]
    )

    #TODO: store task for cancelling later? or can we just disconnect client to kill it?
    asyncio.create_task(self.client.connect())
  
  def create_singleplayer_client(self):
    #TODO: idk how i feel about storing server here
    self.server = LocalServer()
    self.server_game = ServerGame(self.server)
    asyncio.create_task(self.server.start())
    asyncio.create_task(self.server_game.run())

    self.client = LocalClient()
    self.client.setup_handlers(
      connect_handlers=[ClientConnectHandler()],
      event_handlers=[
        E.PongHandler(self),
        E.RoomJoinedHandler(self),
      ]
    )
    asyncio.create_task(self.client.connect(self.server))

  #TODO: split up logic (send HelloLobby and await LobbyUpdated)
  def setup_room_and_lobby(self, room_channel_id, lobby_channel_id):
    self.room_channel = self.client.add_channel(room_channel_id)
    self.room_channel.setup_handlers([
      E.WorldOpenedHandler(self),
      E.WorldClosedHandler(self),
      E.LobbyOpenedHandler(self),
    ])
    lobby_channel = self.client.add_channel(lobby_channel_id)
    self.state = ClientLobbyState(lobby_channel)

  def load_world(self, channel_id):
    channel = self.client.add_channel(channel_id)
    self.state = ClientPlayState(self, channel)
    
  async def run(self):
    while True:
      if self.client is not None:
        self.client.handle_events()
      if self.room_channel is not None:
        self.room_channel.handle_events()
      
      pressed = defaultdict(lambda: False)
      released = defaultdict(lambda: False)
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          pressed[event.key] = True
        if event.type == pygame.KEYUP:
          released[event.key] = True
        if event.type == pygame.QUIT:
          #TODO: need to move this to client game rather than play state
          pygame.quit()
          sys.exit()
      held = pygame.key.get_pressed()

      self.state.step(pressed, held, released)

      #doing both this and clock.tick makes game run as expected, because of course it does
      self.clock.tick(FPS) #limit fps TODO: decouple rendering from physics
      pygame.display.flip()

      self.frames += 1
      if time.time() - self.fps_measure_time > FPS_MEASURE_SECONDS:
        print("[Client] FPS:", self.frames / FPS_MEASURE_SECONDS)
        self.frames = 0
        self.fps_measure_time = time.time()

      await asyncio.sleep(0)
