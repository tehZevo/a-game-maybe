from ecs import World

def floor_transition(generator):
  #TODO: reee
  from components.physics.position import Position
  from components.core.dungeon_floor import DungeonFloor

  world = World()
  world.create_entity([DungeonFloor(generator)])

  return world
