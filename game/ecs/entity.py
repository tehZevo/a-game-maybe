from .component import Component

class Entity:
  def __init__(self):
    self.world = None
    self.components = {}
    #TODO: rename active?
    self.alive = True

  def start(self):
    for component in list(self.components.values()):
      component.start()

  def remove(self):
    self.alive = False

  def on_destroy(self):
    for component in self.components.values():
      component.on_destroy()

  def add_component(self, component):
    #TODO: warn if component type already exists on this entity?
    self.components[component.__class__.__name__] = component
    component.register(self)
  
  def ensure_component(self, component_type):
    component = self.get_component(component_type)
    if component is None:
      component = component_type()
      self.add_component(component)
    return component
    
  def remove_component(self, component):
    #TODO: on remove?
    self.components = {t: c for t, c in self.components.items() if c != component}

  def find(self, component_type):
    return [c for c in self.components.values() if issubclass(c.__class__, component_type)]

  #will return subtypes of the given component type
  def get_component(self, type):
    #TODO: what if we have two subclasses of the same component on the entity?
    for component in self.components.values():
      if issubclass(component.__class__, type):
        return component

  def update(self):
    for c in self.components.values():
      c.update()

  def __repr__(self):
    return "[" + ", ".join([e for e in self.components.keys()]) + "]"
  
  def __iter__(self):
    for c in self.components.values():
      #TODO: remove
      if not isinstance(c, Component):
        raise ValueError(f"{c} is not a component!")
      yield c
    # return iter(self.components.values())

  def __getitem__(self, component_type):
    return self.get_component(component_type)