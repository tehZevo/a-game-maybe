
#TODO: find some way to store world on component so we dont have to entity.world every time
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

  def register(self, entity):
    self.entity = entity
    for rc in self.required_components:
      if entity.get_component(rc) is None:
        entity.add_component(rc())

  def start(self):
    pass

  def on_destroy(self):
    pass

  def update(self):
    pass
