import game.components as C
from ..skill_effect import SkillEffect

class UserHPScaling(SkillEffect):
  def __init__(self, children_f=lambda hp: []):
    super().__init__()
    self.children_f = children_f

  def start(self, skill):
    user_hp = skill.user[C.Stats].stats.secondary.hp

    children = self.children_f(user_hp)
    for child in children:
      skill.entity.world.create_entity([
        C.Position(skill.entity[C.Position].pos),
        C.Skill(child, skill.user, target=skill.target)
      ])
