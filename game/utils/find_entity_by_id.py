#TODO: remove and replace with server/client manager.networked_entities[id]
def find_entity_by_id(world, id):
  #TODO: circular import
  from game.components.networking import Networked
  #this is really expensive...
  #two solutions:
  #A: make "id" a property of ecs entity (and allow creation of entity with specific id)
  #B: keep track of networked entities in a component
  # (i kinda like B)
  ents = world.find(Networked)
  ents = {ent.get_component(Networked).id: ent for ent in ents}
  ent = ents[id] if id in ents else None
  return ent
