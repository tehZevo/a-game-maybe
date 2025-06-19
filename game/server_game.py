import time
import asyncio

import pygame

from game.ecs import World
from game.save_data import SaveData
from game.utils.constants import FPS, DT
import game.networking.commands as commands
import game.components as C
import game.networking.events as E
import game.data.maps as M

class ServerGame:
  def disconnect_handler(self, server, client_id):
    #TODO: really want to avoid having to store server_manager on server...
    server.server_manager.player_unregister(client_id)
    print("client", client_id, "has disconnected")

  def __init__(self, server):
    pygame.init() #TODO: is this needed on the server?
    self.clock = pygame.time.Clock()
    self.save_data = SaveData()
    self.server = server
    
    self.server.setup_handlers(
      disconnect_handlers=[self.disconnect_handler],
      command_handlers=[
        commands.PlayerMoveHandler(),
        commands.PlayerUseSkillHandler(),
        commands.PlayerInteractHandler(),
        commands.SyncHandler(self.save_data),
        commands.PingHandler(),
      ]
    )

    mapdef = M.maze
    world = self.generate_world(mapdef)
    self.world = world
    self.next_world = None
    #TODO: remove/simplify 2-way coupling
    server_manager = self.world.find_component(C.ServerManager)
    self.server.server_manager = server_manager
    
  def generate_world(self, mapdef):
    #create new world
    world = World()
    world.create_entity([C.GameMaster(self, mapdef)])
    
    #add server manager
    server_manager = C.ServerManager()
    world.create_entity([server_manager])
    server_manager.server = self.server

    #generate using mapdef
    mapdef.generator.generate(world, mapdef)
    
    return world

  def transition(self, mapdef):
    world = self.generate_world(mapdef)
    #TODO: broadcast_synced?
    self.server.broadcast(E.WorldClosed())
    self.next_world = world

  async def run(self):
    while True:
      #loop until we have a world to transition to
      while self.next_world is None:
        self.server.handle_commands()

        #update world
        self.world.update()
        #doing both this and clock.tick makes game run as expected, because of course it does
        self.clock.tick(FPS) #limit fps TODO: remove and decouple
        await asyncio.sleep(0)

      #save player data and swap worlds (TODO: use generator spawn method? idk)
      server_manager = self.world.find_component(C.ServerManager)
      for client_id in self.save_data.player_data.keys():
        #TODO: we recreate server manager, so the player map is empty...
        entity_id = server_manager.player_entity_map[client_id]
        ent = server_manager.networked_entities[entity_id]
        self.save_data.save_player_data(client_id, ent)

      self.world = self.next_world
      server_manager = self.world.find_component(C.ServerManager)
      #TODO: remove/simplify 2-way coupling
      self.server.server_manager = server_manager
      self.server.broadcast(E.WorldOpened())
      self.next_world = None
      self.next_server_manager = None
