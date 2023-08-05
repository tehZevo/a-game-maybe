from ecs import Entity

class World:
  def __init__(self):
    self.entities = []

  def create_entity(self, components):
    entity = Entity()
    for component in components:
      entity.add_component(component)
    self.add_entity(entity)

  def add_entity(self, entity):
    self.entities.append(entity)
    entity.world = self
    entity.start()

  #returns all entities with the given component
  def find(self, component_type):
    return [e for e in self.entities if e.get_component(component_type) is not None]

  def update(self):
    for e in self.entities:
      if not e.alive:
        e.on_destroy()
        continue

      e.update()

    #filter dead entities
    self.entities = [e for e in self.entities if e.alive]
