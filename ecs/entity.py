
class Entity:
  def __init__(self):
    self.world = None
    self.components = {}
    #TODO: rename active?
    self.alive = True

  def start(self):
    for component in self.components.values():
      component.start()

  def remove(self):
    self.alive = False

  def add_component(self, component):
    #TODO: warn if component type already exists on this entity?
    component.register(self)
    self.components[component.__class__.__name__] = component

  def get_component(self, type):
    return None if type.__name__ not in self.components else self.components[type.__name__]

  def update(self):
    for c in self.components.values():
      c.update()
