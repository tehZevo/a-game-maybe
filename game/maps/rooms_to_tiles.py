import random

from game.tiles import Floor, Wall, TileType

def rooms_to_tiles(rooms, room_size, door_width, accent):
  def is_not_doorway(u, v, n, exit):
    if u == n:
      if exit:
        return v < door_width or v >= room_size - door_width
      return True
    return False

  def is_wall(x, y, north, south, east, west):
    return \
      is_not_doorway(x, y, 0, west) or \
      is_not_doorway(x, y, room_size - 1, east) or \
      is_not_doorway(y, x, 0, north) or \
      is_not_doorway(y, x, room_size - 1, south)

  tiles = {}
  for rx, ry, north, south, east, west in rooms:
    for tx in range(room_size):
      for ty in range(room_size):
        if is_wall(tx, ty, north, south, east, west):
          tile_type = TileType.WALL_ACCENT if random.random() < accent else TileType.WALL
          tile = Wall(type=tile_type)
        else:
          tile_type = TileType.FLOOR_ACCENT if random.random() < accent else TileType.FLOOR
          tile = Floor(type=tile_type)

        x = rx * room_size + tx
        y = ry * room_size + ty
        tiles[(x, y)] = tile
  return tiles