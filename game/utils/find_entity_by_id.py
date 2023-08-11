def find_entity_by_id(world, id):
  #TODO: circular import
  from game.components.networking import Id
  #this is really expensive...
  #two solutions:
  #A: make "id" a property of ecs entity (and allow creation of entity with specific id)
  #B: keep track of networked entities in a component
  # (i kinda like B)
  ents = world.find(Id)
  ents = {ent.get_component(Id).id: ent for ent in ents}
  ent = ents[event.id] if event.id in ents else None
  return ent
