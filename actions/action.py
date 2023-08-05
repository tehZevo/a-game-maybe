
class Action:
  def __init__(self):
    self.interruptible = True
    self.entity = None
    self.active = False

  #shorthand
  def get_component(self, type):
    return self.entity.get_component(type)

  def register(self, entity):
    self.entity = entity

  def init(self):
    pass

  def update(self):
    pass
