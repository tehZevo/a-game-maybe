from ecs import Component

#TODO: rename dungeon generator?
class DungeonFloor(Component):
  def __init__(self, generator):
    super().__init__()
    self.generator = generator

  def start(self):
    self.generator.generate(self.entity)
    #TODO: alive=false after running?
