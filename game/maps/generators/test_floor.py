import game.components as C
from game.tiles import Wall, Floor, Tileset
from game.utils import Vector
from .floor_generator import FloorGenerator

from game.monsters import slime
from game.items import Hat, SkillItem
from game.skills import test_alpha_skill

class TestFloor(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.width = 40
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

        tiles[y][x] = tile

    ts = Tileset(self.width, self.height, tiles)
    world.create_entity([C.TilesetPhysics(ts)])

    #create stairs to this generator
    world.create_entity([C.Position(self.stairs_pos), C.Stairs(self)])

    world.create_entity([C.Position(Vector(8, 9)), C.Chest([Hat(), SkillItem(test_alpha_skill)])])

    world.create_entity([C.Position(self.spawner_pos), C.Spawner(slime)]) #TODO: hardcoded mobdef

    # #TODO: need separate spawn function that creates players with given player data
    # world.create_entity([C.Position(self.player_spawn), C.Player()])
