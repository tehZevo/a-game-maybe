from ecs import Component

class Position(Component):
  def __init__(self, x=0, y=0):
    super().__init__()
    self.set_pos(x, y)

  def set_pos(self, x, y):
    self.x = x
    self.y = y

  def get_pos(self):
    return [self.x, self.y]
