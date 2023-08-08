from ecs import Component
from components import Position

#TODO: rename to SkillInstance?
class Skill(Component):
  def __init__(self, effect, user, parent=None):
    super().__init__()
    self.require(Position)
    self.effect = effect
    self.user = user
    self.parent = parent

  def start(self):
    self.effect.register(self.entity, self.user, self.parent)
    self.effect.start()

  def update(self):
    self.effect.update()
    if self.effect.completed:
      self.alive = False
