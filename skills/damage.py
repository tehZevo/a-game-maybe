from skills import SkillEffect
from components import Actor

class Damage(SkillEffect):
  def __init__(self, power=100):
    super().__init__()
    self.target = None
    self.power = power

  def start(self):
    #TODO: how to get targets?
    #TODO: we could just set them on children manually lol
    #TODO: damage calcs
    self.target.get_component(Actor).damage(self.power / 100.)
