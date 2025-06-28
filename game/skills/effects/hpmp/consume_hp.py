import game.components as C
from ..skill_effect import SkillEffect

class ConsumeHP(SkillEffect):
  def __init__(self, percent=10):
    super().__init__()
    self.percent = percent

  def start(self, skill):
    #TODO: invuln check + ignore_invuln param so player can self target?
    #TODO: or raise invlun check to targeting itself?
    stats = skill.user[C.Stats].stats.secondary
    skill.user[C.Actor].damage(stats.hp * self.percent / 100)
