
#TODO: make ABC
class Component:
  def __init__(self):
    self.required_components = set()

  def require(self, type):
    self.required_components.add(type)

  def init(self, entity):
    for rc in self.required_components:
      if entity.get_component(rc) is None:
        entity.add_component(rc())

  def update(self, entity):
    pass
