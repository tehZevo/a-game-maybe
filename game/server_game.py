import pygame, sys
from pygame.math import Vector2

from game.ecs import World
from game.save_data import SaveData
from game.utils.constants import FPS
from game.utils.floor_transition import floor_transition
from game.floor_generators import TestFloor, DFSGenerator
from game.networking import Server
from game.networking.server_connect_handler import ServerConnectHandler
from game.networking.commands import PlayerMoveHandler, PlayerUseSkillHandler, PlayerInteractHandler
from game.utils import Vector
import game.components as C

class ServerGame:
  def __init__(self):
    pygame.init() #TODO: is this needed on the server?
    self.clock = pygame.time.Clock()
    
    self.save_data = SaveData()

    self.server = Server(
      connect_handlers=[ServerConnectHandler(self.save_data)],
      command_handlers=[
        PlayerMoveHandler(),
        PlayerUseSkillHandler(),
        PlayerInteractHandler(),
      ],
    )
    self.server.start()

    world = self.generate_world()
    self.world = world
    #TODO: remove/simplify 2-way coupling
    server_manager = self.world.find_component(C.ServerManager)
    self.server.server_manager = server_manager
    
    floor_transition(self.world, DFSGenerator())
    # floor_transition(self.world, TestFloor())

    self.next_world = None
    self.init_world(self.save_data)

  def generate_world(self):
    world = World()

    #create server manager
    server_manager = C.ServerManager()
    world.create_entity([server_manager])
    server_manager.server = self.server
    
    return world

  #TODO: merge some of this with generate world?
  def init_world(self, save_data):
    
    #store reference to game as an entity
    self.world.create_entity([C.GameMaster(self)])
    server_manager = self.world.find_component(C.ServerManager)
    #create players and apply save data
    for client_id in save_data.player_data.keys():
      player = self.world.create_entity([
        C.Networking(),
        C.Position(Vector(2, 2)), #TODO: hardcoded position
        C.Player(),
      ])

      entity_id = player.get_component(C.Networking).id
      server_manager.player_register(client_id, entity_id)
      save_data.load_player_data(client_id, player)
  
  #TODO: use a "mapdef" instead of a world_gen_func
  def transition(self, world_gen_func):
    world = self.generate_world()
    world_gen_func(world)
    self.next_world = world

  def run(self):
    while True:
      #loop until we have a world to transition to
      while self.next_world is None:
        #update world
        self.world.update()

        self.clock.tick(FPS) #limit fps TODO: remove and decouple

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
      self.init_world(self.save_data)
      #grab new server manager and tell players about their new entities
      #tell players about their new entities
      from game.networking.events import PlayerAssigned
      for client_id, entity_id in server_manager.player_entity_map.items():
        self.server.send(client_id, PlayerAssigned(entity_id))
      self.next_world = None
      self.next_server_manager = None
