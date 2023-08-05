
#TODO: make ABC
class Component:
  def __init__(self):
    self.entity = None
    self.required_components = set()

  def require(self, type):
    self.required_components.add(type)

  #shorthand
  def get_component(self, type):
    return self.entity.get_component(type)

  def init(self, entity):
    self.entity = entity
    for rc in self.required_components:
      if entity.get_component(rc) is None:
        entity.add_component(rc())

  def update(self):
    pass
