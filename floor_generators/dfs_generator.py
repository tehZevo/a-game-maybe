import random

from floor_generators import FloorGenerator
from components.tiles.floor import Floor
from components.tiles.wall import Wall
from components.tiles.stairs import Stairs
from components.tiles.spawner import Spawner
from components.physics.position import Position
from components.actor.player import Player
from components.actor.enemy import Enemy
from utils import Vector

class DFSGenerator(FloorGenerator):
  def __init__(self):
    super().__init__()
    self.floor_size = 2 #in number of rooms wide/tall
    self.room_size = 8
    self.door_width = 2
    self.player_spawn = Vector(2, 2)
    self.spawner_pos = Vector(10, 10)
    self.stairs_pos = Vector(3, 10)

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

    for x, y, north, south, east, west in rooms:
      for rx in range(self.room_size):
        for ry in range(self.room_size):
          if is_wall(rx, ry, north, south, east, west):
            world.create_entity([Position(Vector(x * self.room_size + rx, y * self.room_size + ry)), Wall()])
          else:
            world.create_entity([Position(Vector(x * self.room_size + rx, y * self.room_size + ry)), Floor()])

    #create stairs to this generator
    world.create_entity([Position(self.stairs_pos), Stairs(self)])

    world.create_entity([Position(self.spawner_pos), Spawner(Enemy)])
    #TODO: need separate spawn function that creates players with given player data
    world.create_entity([Position(self.player_spawn), Player()])
