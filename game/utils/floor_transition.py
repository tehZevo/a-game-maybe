from game.ecs import World
from game.components.core import DungeonFloor

def floor_transition(generator):

  world = World()
  world.create_entity([DungeonFloor(generator)])

  return world
