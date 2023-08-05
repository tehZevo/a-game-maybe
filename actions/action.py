
class Action:
  def __init__(self):
    self.interruptible = True
    self.entity = None
    self.active = False

  def register(self, entity):
    self.entity = entity

  def init(self):
    pass

  def update(self):
    pass
