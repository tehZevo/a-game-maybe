import game.components as C

def find_in_range(world, component_type, pos, radius):
  ents = world.find(component_type)
  ents = [e for e in ents if e.get_component(C.Position).pos.distance(pos) <= radius]
  #TODO: sort by distance?
  # ents.sort()
  return ents
