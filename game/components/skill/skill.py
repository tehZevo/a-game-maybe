from game.ecs import Component
import game.components as C

#TODO: move to actor?
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
    import game.skills.effects as E
    #TODO: bad
    is_client = self.entity.world.find_component(C.ClientManager) is not None
    if is_client and not isinstance(self.effect, (E.Rush, E.SelfTarget)):
      return
    self.state = self.effect.start(self)

  def update(self):
    self.state = self.effect.update(self, self.state)
    if self.completed:
      self.alive = False
      self.effect.remove(self, self.state)
