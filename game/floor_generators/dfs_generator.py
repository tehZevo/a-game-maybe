import random

from game.floor_generators import FloorGenerator
from game.components.tiles import Stairs, Spawner
from game.components.physics import Position
from game.components.actor import Enemy, Player
from game.components.graphics import BakedTileset
from game.components.tiles import TilesetPhysics
from game.tiles import Tileset, Floor, Wall
from game.utils import Vector

SPAWNER_CHANCE = 0.5

class DFSGenerator(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.floor_size = 4 #in number of rooms wide/tall
    self.room_size = 8
    self.door_width = 2

  def build_dfs(self):
    def oob(x, y):
      return x < 0 or y < 0 or x >= self.floor_size or y >= self.floor_size

    depth = 0
    grid = [[None for _ in range(self.floor_size)] for _ in range(self.floor_size)]
    queue = []
    visited = set()
    queue.append((random.randint(0, self.floor_size - 1), random.randint(0, self.floor_size - 1)))
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while len(queue) > 0:
      #visit tail
      pos = queue[-1]
      visited.add(pos)
      #write depth to grid
      grid[pos[0]][pos[1]] = len(queue)

      #visit random valid neighbor
      dirs2 = dirs.copy()
      random.shuffle(dirs2)
      valid_dir_found = False
      for dir in dirs2:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos in visited:
          continue
        #skip oob
        if oob(new_pos[0], new_pos[1]):
          continue
        queue.append(new_pos)
        valid_dir_found = True
        break
      if not valid_dir_found:
        queue.pop()

    #convert int grid to rooms
    rooms = []
    for y in range(self.floor_size):
      for x in range(self.floor_size):
        center = grid[x][y]
        north = False if oob(x, y-1) else abs(grid[x][y-1] - center) == 1
        south = False if oob(x, y+1) else abs(grid[x][y+1] - center) == 1
        east = False if oob(x+1, y) else abs(grid[x+1][y] - center) == 1
        west = False if oob(x-1, y) else abs(grid[x-1][y] - center) == 1
        room = [x, y, north, south, east, west]
        rooms.append(room)
    return rooms

  def generate(self, world):
    rooms = self.build_dfs()
    def is_not_doorway(u, v, n, exit):
      if u == n:
        if exit:
          return v < self.door_width or v >= self.room_size - self.door_width
        return True
      return False

    def is_wall(x, y, north, south, east, west):
      return \
        is_not_doorway(x, y, 0, west) or \
        is_not_doorway(x, y, self.room_size - 1, east) or \
        is_not_doorway(y, x, 0, north) or \
        is_not_doorway(y, x, self.room_size - 1, south)

    tileset = Tileset(self.room_size * self.floor_size, self.room_size * self.floor_size)
    for rx, ry, north, south, east, west in rooms:
      #randomly create spawners
      if random.random() < SPAWNER_CHANCE:
        world.create_entity([
          Position(Vector(rx * self.room_size + self.room_size / 2, ry * self.room_size + self.room_size / 2)),
          Spawner(Enemy, radius=2, wave_time=2, wave_count=1, spawn_max=3)
        ])
      for tx in range(self.room_size):
        for ty in range(self.room_size):
          tile = Wall() if is_wall(tx, ty, north, south, east, west) else Floor()
          x = rx * self.room_size + tx
          y = ry * self.room_size + ty
          tileset.set_tile(x, y, tile)

    world.create_entity([TilesetPhysics(tileset)])

    #choose random room to put stairs in
    x, y, _, _, _, _ = random.choice(rooms)
    #create stairs to this generator
    world.create_entity([Position(Vector(x * self.room_size + self.room_size / 2, x * self.room_size + self.room_size / 2)), Stairs(self)])

    #choose random room to spawn player in
    x, y, _, _, _, _ = random.choice(rooms)
    #TODO: need separate spawn function that creates players with given player data
    world.create_entity([Position(Vector(x * self.room_size + self.room_size / 2, x * self.room_size + self.room_size / 2)), Player()])
