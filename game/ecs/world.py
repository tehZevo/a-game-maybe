from itertools import chain

from game.ecs import Entity

class World:
  def __init__(self):
    self.entities = []

  def create_entity(self, components):
    entity = Entity()
    for component in components:
      entity.add_component(component)
    self.add_entity(entity)

    return entity

  def add_entity(self, entity):
    #TODO: need to prevent ability of adding a new entity to the list from another thread
    # may have to add to a separate list and then concat with main list adfter update
    #TODO: lock?
    self.entities.append(entity)
    entity.world = self
    entity.start()

  #returns all entities with the given component
  def find(self, component_type):
    return [e for e in self.entities if e.get_component(component_type) is not None]

  def find_components(self, component_type):
    #return ALL components that match
    return list(chain.from_iterable([e.find(component_type) for e in self.find(component_type)]))

  def update(self):
    #copy entity list so we don't iterate over newly created entities
    ents = self.entities.copy()

    for e in ents:
      e.update()

    for e in ents:
      if not e.alive:
        e.on_destroy()

    #filter dead entities in original entity list
    self.entities = [e for e in self.entities if e.alive]
