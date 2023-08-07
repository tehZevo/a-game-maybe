from ecs import World

def floor_transition(generator):
  #TODO: reee
  from components import Position, DungeonFloor

  world = World()
  world.create_entity([DungeonFloor(generator)])

  return world
