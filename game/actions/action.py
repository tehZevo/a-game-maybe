#by default, actions are interruptible and immediately end
class Action:
  def __init__(self):
    self.interruptible = True
    self.entity = None
    #TODO: rename done?
    self.active = False

  #shorthand
  def get_component(self, type):
    return self.entity.get_component(type)

  def register(self, entity):
    self.entity = entity

  def start(self):
    pass

  #TODO: have def end or interrupted?

  def update(self):
    pass
