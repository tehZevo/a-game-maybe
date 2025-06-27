import random

from .floor_generator import FloorGenerator
from game.components.tiles import Stairs, Spawner
from game.components.physics import Position

import game.data.mobs as Mobs
from game.utils import Vector
import game.components as C
from game.data.registry import get_map
from game.maps.rooms_to_tiles import rooms_to_tiles

class DFSGenerator(FloorGenerator):
  def __init__(self, room_size=8, floor_size=3, door_width=2, accent=1/10, spawner_chance=0.25, next_maps=[]):
    super().__init__()
    #in number of rooms wide/tall
    self.floor_size = floor_size
    self.room_size = room_size
    self.door_width = door_width
    self.accent = accent
    self.next_maps = next_maps
    self.spawner_chance = spawner_chance

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

  def generate(self, mapdef):
    rooms = self.build_dfs()
    tiles = rooms_to_tiles(rooms, self.room_size, self.door_width, self.accent)
    entities = []
    
    for rx, ry, _, _, _, _ in rooms:
      #randomly create spawners
      if random.random() < self.spawner_chance:
        entities.append([
          Position(Vector(rx * self.room_size + self.room_size / 2, ry * self.room_size + self.room_size / 2)),
          Spawner(Mobs.slime, radius=2, wave_time=5, wave_count=4, spawn_max=4) #TODO: hardcoded mobdef
        ])

    #choose random room to put stairs in
    x, y, _, _, _, _ = random.choice(rooms)
    stairs_pos = Vector(x * self.room_size + self.room_size / 2, x * self.room_size + self.room_size / 2)
    next_map_id = random.choice(self.next_maps) if len(self.next_maps) > 0 else mapdef
    next_map = get_map(next_map_id)
    entities.append([Position(stairs_pos), Stairs(next_map)])

    return tiles, entities
