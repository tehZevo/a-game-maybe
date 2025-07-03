import random

from .floor_generator import FloorGenerator
from game.components.tiles import Stairs, Spawner
from game.components.physics import Position

from game.tiles import Floor, Wall, TileType
import game.data.mobs as Mobs
from game.utils import Vector
import game.components as C
from game.data.registry import get_map
from game.maps.rooms_to_tiles import rooms_to_tiles
import game.data.items as I
import game.data.maps as M

class DevMapGenerator(FloorGenerator):
  def __init__(self):
    super().__init__()

  def generate(self, mapdef):
    rooms = [[0, 0, False, False, False, False]]
    tiles = rooms_to_tiles(rooms, 16, 0, 0)
    entities = []

    dev_chests = [
      [I.dev_die, I.dev_heal, I.dev_rush, I.unobtanium_shortsword],
      [I.staff_of_healing, I.wooden_shortsword],
      [I.sacrifice, I.sanguine_strike],
      [I.bless, I.magic_bolt, I.fireball, I.heal, I.heal_burst],
    ]
    
    for i, loot in enumerate(dev_chests):
      entities.append([C.Position(Vector(4 + i * 2, 4)), C.Chest(loot)])

    entities.append([Position(Vector(8, 8)), Stairs(M.maze)])

    return tiles, entities
