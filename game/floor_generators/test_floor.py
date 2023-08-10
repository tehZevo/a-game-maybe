from floor_generators import FloorGenerator
from components.tiles.spawner import Spawner
from components.tiles.stairs import Stairs
from components.physics.position import Position
from components.actor.player import Player
from components.actor.enemy import Enemy
from tiles.wall import Wall
from tiles.floor import Floor
from tiles.tileset import Tileset
from utils import Vector

class TestFloor(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.width = 20
    self.height = 20
    self.player_spawn = Vector(2, 2)
    self.spawner_pos = Vector(10, 10)
    self.stairs_pos = Vector(3, 10)

  def generate(self, world):
    tiles = [[None for _ in range(self.width)] for _ in range(self.height)]
    for x in range(self.width):
      for y in range(self.height):
        tile = None
        if x == 0 or x == self.width - 1 or y == 0 or y == self.height -1:
          tile = Wall()
        else:
          tile = Floor()

        tiles[x][y] = tile

    world.create_entity([Tileset(tiles)])

    #create stairs to this generator
    world.create_entity([Position(self.stairs_pos), Stairs(self)])

    world.create_entity([Position(self.spawner_pos), Spawner(Enemy)])
    #TODO: need separate spawn function that creates players with given player data
    world.create_entity([Position(self.player_spawn), Player()])
