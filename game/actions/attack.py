import game.components as C
from . import Action
import game.data.skills as S
import game.actions as A

class Attack(Action):
  def deserialize(action_data):
    return Attack()

  def __init__(self):
    super().__init__()
    self.interruptible = False
  
  def serialize(self):
    return {}

  def start(self):
    self.entity.get_component(C.Actor).act(A.UseSkill(S.default_attack))
