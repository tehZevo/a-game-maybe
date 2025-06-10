import game.components as C

#TODO: remove and replace with server/client manager.networked_entities[id]
def find_entity_by_id(world, id):
  #this is really expensive...
  ents = world.find(C.Networking)
  ents = {ent.get_component(C.Networking).id: ent for ent in ents}
  ent = ents[id] if id in ents else None
  return ent
