from game.ecs import Component

class Id(Component):
  def __init__(self, id):
    super().__init__()
    self.id = id
