
class World:
  def __init__(self):
    self.entities = []

  def add_entity(self, entity):
    self.entities.append(entity)
    entity.init(self)

  #returns all entities with the given component
  def find(self, component_type):
    return [e for e in self.entities if e.get_component(component_type) is not None]

  def update(self):
    for e in self.entities:
      e.update()

    #filter dead entities
    self.entities = [e for e in self.entities if e.alive]
