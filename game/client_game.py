import time
import asyncio

import pygame

from game.constants import FPS, TILE_SIZE, DT
import game.networking.events as E
import game.networking.commands as C

from game.states import ClientPlayState, ClientLobbyState

#TODO: end game state when world closes
#TODO: add world opened handler to lobby state or some kind of loading state

#TODO: move to constants?
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
FPS_MEASURE_SECONDS = 10

class DummyState:
  def step(self):
    pass

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
  def __init__(self, client, scale_res=1):
    pygame.init()
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

    self.client = client
    self.client.setup_handlers(
      connect_handlers=[ClientConnectHandler()],
      event_handlers=[
        E.PongHandler(self),
        E.RoomJoinedHandler(self),
      ]
    )

    self.state = DummyState()
  
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
      self.client.handle_events()
      if self.room_channel is not None:
        self.room_channel.handle_events()
      self.state.step()

      #doing both this and clock.tick makes game run as expected, because of course it does
      self.clock.tick(FPS) #limit fps TODO: decouple rendering from physics
      pygame.display.flip()

      self.frames += 1
      if time.time() - self.fps_measure_time > FPS_MEASURE_SECONDS:
        print("[Client] FPS:", self.frames / FPS_MEASURE_SECONDS)
        self.frames = 0
        self.fps_measure_time = time.time()

      await asyncio.sleep(0)
