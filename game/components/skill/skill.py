from game.ecs import Component
import game.components as C

class Skill(Component):
  def __init__(self, effect, user, parent=None, target=None):
    super().__init__()
    self.require(C.Position)
    self.effect = effect
    self.user = user
    self.parent = parent
    self.target = target
    self.completed = True
    self.state = None

  def start(self):
    self.state = self.effect.start(self)

  def update(self):
    self.state = self.effect.update(self, self.state)
    if self.completed:
      self.alive = False
      self.effect.remove(self, self.state)
