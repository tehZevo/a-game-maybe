from ecs import Component
from components import Physics, Sprite

class Actor(Component):
  def __init__(self):
    super().__init__()
    self.require(Physics)
    self.require(Sprite)
    self.action = None
    self.next_action = None

  def start_action(self, action):
    self.action = action
    self.action.register(self)
    self.action.init()

  def act(self, action):
    if self.action is None or self.action.interruptible:
      self.start_action(action)
    else:
      self.next_action = action

  def update(self):
    #update current action
    if self.action is not None:
      self.action.update()

      #start new action if old action is finished
      if not self.action.active:
        self.start_action(self.next_action)
        self.next_action = None
