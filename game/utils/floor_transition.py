from game.ecs import World

def floor_transition(world, generator):
  #TODO: circular import
  from game.components.core import DungeonFloor
  world.create_entity([DungeonFloor(generator)])
