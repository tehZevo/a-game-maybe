from collections import defaultdict
from itertools import chain

from game.ecs import Entity

class World:
  def __init__(self):
    self.entities = []
    self.lookup = defaultdict(list)

  def create_entity(self, components):
    entity = Entity()
    for component in components:
      entity.add_component(component)
    self.add_to_lookup(entity)
    self.add_entity(entity)

    return entity

  #TODO: add to lookup when adding/remove components in entity
  #TODO: entity dity flag?
  def add_to_lookup(self, entity):
    for c in entity:
      self.lookup[c.__class__].append(entity)

  def remove_from_lookup(self, entity):
    for c in entity:
      self.lookup[c.__class__] = [e for e in self.lookup[c.__class__] if e != entity]

  def add_entity(self, entity):
    entity.world = self
    self.entities.append(entity)
    entity.start()

  #returns all entities with the given component
  def find(self, component_type):
    found_entities = []
    for lookup_type, entities in self.lookup.items():
      if issubclass(lookup_type, component_type):
        found_entities += entities
    return found_entities
  
  def find_components(self, component_type):
    entities = self.find(component_type)
    return [e.get_component(component_type) for e in entities]

  #shorthand
  def find_component(self, component_type):
    comps = self.find_components(component_type)
    if len(comps) == 0:
      return None
    return comps[0]

  def update(self):
    #copy entity list so we don't iterate over newly created entities
    ents = self.entities.copy()

    for e in ents:
      e.update()

    for e in ents:
      if not e.alive:
        e.on_destroy()
        self.remove_from_lookup(e)

    #filter dead entities in original entity list
    self.entities = [e for e in self.entities if e.alive]

  def __getitem__(self, component_type):
    return self.find_components(component_type)
