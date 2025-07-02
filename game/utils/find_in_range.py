import game.components as C

def find_in_range(world, component_type, pos, radius, sort=False):
  ents = world.find(component_type)
  ents = [(e[C.Position].pos.distance(pos), e) for e in ents]
  ents = [(dist, e) for dist, e in ents if dist <= radius]

  if sort:
    ents.sort(key=lambda x: x[0])
  
  ents = [e for _, e in ents]
  
  return ents
