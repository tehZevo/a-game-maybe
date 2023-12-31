import pygame, sys
from pygame.math import Vector2

from game.ecs import World
from game.save_data import SaveData
from game.components.core import GameMaster
from game.components.networking import ServerManager
from game.utils.constants import FPS
from game.utils.floor_transition import floor_transition
from game.floor_generators import TestFloor, DFSGenerator

class ServerGame:
  def __init__(self):
    pygame.init() #TODO: is this needed on the server?
    self.clock = pygame.time.Clock()

    #TODO: store a party (player game/"save" data) so player data can be repopulated on the new floor
    self.world = self.generate_world()
    # floor_transition(self.world, DFSGenerator())
    floor_transition(self.world, TestFloor())

    self.next_world = None
    self.init_world()

  def generate_world(self):
    #TODO: rename to game_world?
    world = World()

    #create server
    #TODO: actually.. maybe server should exist outside lol...
    # that or we should create a server first and then pass the existing one to the Server component
    world.create_entity([
      ServerManager()
    ])
    return world

  def init_world(self, save_data=None):
    #TODO: load player data
    #store reference to game as an entity
    self.world.create_entity([GameMaster(self)])

    #apply save data
    if save_data is not None:
      save_data.apply(self.world)

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

      #swap worlds, create new player (TODO: use generator spawn method? idk)
      save_data = SaveData(self.world)
      self.world = self.next_world
      self.init_world(save_data)
      self.next_world = None
