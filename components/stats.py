from ecs import Component

class Stats(Component):
  def __init__(self):
    super().__init__()
    #TODO: calculate
    self.move_speed = 1
    self.hp = 100
    self.mp = 100
