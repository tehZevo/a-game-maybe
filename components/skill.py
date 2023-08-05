from ecs import Component
from components import Position

#TODO: store user (actor entity)?
class Skill(Component):
  def __init__(self, effect):
    super().__init__()
    self.require(Position)
    self.effect = effect

  def start(self):
    self.effect.register(self.entity)
    self.effect.start()

  def update(self):
    self.effect.update()
    if self.effect.completed:
      self.alive = False
