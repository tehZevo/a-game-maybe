from ecs import Component
from components import Physics, Sprite, Stats, ItemDropper, Equips

class Actor(Component):
  def __init__(self):
    super().__init__()
    self.require(Physics)
    self.require(Sprite)
    self.require(Stats)
    self.require(ItemDropper)
    self.require(Equips)
    self.action = None
    self.next_action = None

  def damage(self, amount):
    stats = self.get_component(Stats)
    stats.hp -= amount

  def start_action(self, action):
    self.action = action
    self.action.register(self.entity)
    self.action.start()

  def act(self, action):
    if self.action is None or self.action.interruptible:
      self.start_action(action)
    else:
      self.next_action = action

  def update(self):
    stats = self.get_component(Stats)
    if stats.hp <= 0:
      self.entity.remove()

    if not self.entity.alive:
      return

    #update current action
    if self.action is not None:
      self.action.update()

      #start new action if old action is finished
      if not self.action.active and self.next_action is not None:
        self.start_action(self.next_action)
        self.next_action = None
