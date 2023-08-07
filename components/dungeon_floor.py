from ecs import Component

class DungeonFloor(Component):
  def __init__(self, generator):
    super().__init__()
    self.generator = generator

  def start(self):
    self.generator.generate(self.entity)
