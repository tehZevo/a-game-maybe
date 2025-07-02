import game.components as C
from . import Action
import game.data.skills as S
import game.actions as A
from game.items.slots import WeaponSlot

class Attack(Action):
  def deserialize(action_data):
    return Attack()

  def __init__(self):
    super().__init__()
    self.interruptible = False
  
  def serialize(self):
    return {}

  def start(self):
    equips = self.entity[C.Equips]
    weapon = equips.weapons[WeaponSlot.PRIMARY]
    weapon_skill = weapon and weapon.attack_skill
    skill = weapon_skill if weapon_skill is not None else S.default_attack
    self.entity.get_component(C.Actor).act(A.UseSkill(skill))
