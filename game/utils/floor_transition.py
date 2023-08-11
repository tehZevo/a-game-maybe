from game.ecs import World

def floor_transition(generator):
  #TODO: circular import
  from game.components.core import DungeonFloor
  world = World()
  world.create_entity([DungeonFloor(generator)])

  return world
