from .action_registry import get_action_classes

#by default, actions are interruptible and immediately end
class Action:
  def deserialize(action_type, action_data):
    action_class = get_action_classes()[action_type]
    action = action_class.deserialize(action_data)
    return action

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
  
  def serialize(self):
    raise NotImplementedError
