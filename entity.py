
class Entity:
  def __init__(self):
    self.components = {}

  def add_component(self, component):
    #TODO: warn if component type already exists on this entity?
    component.init(self)
    self.components[component.__class__.__name__] = component

  def get_component(self, type):
    return None if type.__name__ not in self.components else self.components[type.__name__]

  def update(self):
    for c in self.components.values():
      c.update(self)
