from floor_generators import FloorGenerator
from components.tiles.floor import Floor
from components.tiles.wall import Wall
from components.tiles.stairs import Stairs
from components.tiles.spawner import Spawner
from components.physics.position import Position
from components.actor.player import Player
from components.actor.enemy import Enemy
from utils import Vector

class TestFloor(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.width = 20
    self.height = 20
    self.player_spawn = Vector(2, 2)
    self.spawner_pos = Vector(10, 10)
    self.stairs_pos = Vector(3, 10)

  def generate(self, floor_entity):
    for x in range(self.width):
      for y in range(self.height):
        if x == 0 or x == self.width - 1 or y == 0 or y == self.height -1:
          floor_entity.world.create_entity([Position(Vector(x, y)), Wall()])
        else:
          floor_entity.world.create_entity([Position(Vector(x, y)), Floor()])

    #create stairs to this generator
    floor_entity.world.create_entity([Position(self.stairs_pos), Stairs(self)])

    floor_entity.world.create_entity([Position(self.spawner_pos), Spawner(Enemy)])
    #TODO: need separate spawn function that creates players with given player data
    floor_entity.world.create_entity([Position(self.player_spawn), Player()])
