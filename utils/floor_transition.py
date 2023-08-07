from ecs import World

def floor_transition(player, generator):
  #TODO: reee
  from components import Position, DungeonFloor

  world = World()
  player.get_component(Position).pos = generator.player_spawn
  world.create_entity([DungeonFloor(generator)])
  world.add_entity(player)

  return world
