from uuid import uuid4
import time
import asyncio

import pygame

from game.ecs import World
from game.save_data import SaveData
from game.constants import FPS, DEV_ROOM_CODE
import game.networking.commands as C
import game.data.maps as M
from game.utils import create_join_code

from .server_room import ServerRoom

class ServerGame:
  def disconnect_handler(self, client_id):
    print("[Server] Client", client_id, "has disconnected")
    room_id = self.client_room_mapping[client_id]
    room = self.rooms[room_id]
    room.on_disconnect(client_id)
  
  def connect_handler(self, client_id):
    print("[Server] Client", client_id, "connected")

  def __init__(self, server):
    pygame.init() #TODO: is this needed on the server?
    self.clock = pygame.time.Clock()
    self.server = server
    
    self.server.setup_handlers(
      disconnect_handlers=[self.disconnect_handler],
      connect_handlers=[self.connect_handler],
      command_handlers=[
        C.CreateRoomHandler(self),
        C.JoinRoomHandler(self),
        C.PingHandler(self),
      ]
    )

    self.rooms = {}
    self.client_room_mapping = {}
  
  def create_room(self, initial_mapdef_id=None):
    join_code = DEV_ROOM_CODE or create_join_code()
    while join_code in self.rooms:
      join_code = create_join_code()
    
    channel = self.server.create_channel()
    room = ServerRoom(self.server, channel, join_code, initial_mapdef_id)
    self.rooms[join_code] = room

    return room, join_code

  async def run(self):
    while True:
      self.server.handle_commands()
      #TODO: make each room loop itself separately?
      for room in self.rooms.values():
        room.step()
        if room.empty:
          print("[Server] Room", room.join_code, "empty, closing...")
      
      self.rooms = {k: v for k, v in self.rooms.items() if not v.empty}
      
      self.clock.tick(FPS)
      await asyncio.sleep(0)
