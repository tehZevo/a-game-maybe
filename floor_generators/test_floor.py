from floor_generators import FloorGenerator
from components.tiles import Floor, Wall
from components import Position
from utils import Vector

class TestFloor(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.width = 20
    self.height = 20
    self.player_spawn = Vector(2, 2)
    self.spawner_pos = Vector(5, 5)

  def generate(self, floor_entity):
    for x in range(self.width):
      for y in range(self.height):
        if x == 0 or x == self.width - 1 or y == 0 or y == self.height -1:
          floor_entity.world.create_entity([Position(Vector(x, y)), Wall()])
        else:
          floor_entity.world.create_entity([Position(Vector(x, y)), Floor()])

    #TODO: create player and spawner
