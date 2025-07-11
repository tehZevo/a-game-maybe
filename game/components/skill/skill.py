from game.ecs import Component
import game.components as C
import game.skills.effects as E

#TODO: move to actor folder?
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
    #TODO: multiplier field that other things can set (e.g. consume % hp -> multiplier?)

  def start(self):
    #TODO: bad
    is_client = self.entity.world.find_component(C.ClientManager) is not None
    if is_client and not isinstance(self.effect, (E.Rush, E.SelfTarget)):
      return
    self.state = self.effect.start(self)

  def update(self):
    #TODO: bad
    is_client = self.entity.world.find_component(C.ClientManager) is not None
    if is_client and not isinstance(self.effect, (E.Rush, E.SelfTarget)):
      return
    self.state = self.effect.update(self, self.state)
    if self.completed:
      self.entity.remove()
      self.effect.remove(self, self.state)
