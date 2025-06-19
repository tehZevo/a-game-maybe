from enum import IntEnum

from .vector import Vector

Direction = IntEnum("Direction", ["EAST, NORTH, WEST, SOUTH"])

#assumes normalized
def vector_to_direction(v):
  if v.x > 0.5: return Direction.EAST
  if v.x < -0.5: return Direction.WEST
  if v.y > 0.5: return Direction.SOUTH
  if v.y > -0.5: return Direction.NORTH

def direction_to_vector(d):
  match d:
    case Direction.EAST: return Vector(1, 0)
    case Direction.WEST: return Vector(-1, 0)
    case Direction.NORTH: return Vector(0, -1) #TODO: y up? :pleading:
    case Direction.SOUTH: return Vector(0, 1)
