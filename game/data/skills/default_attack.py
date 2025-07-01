import game.skills.effects as E
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType

default_attack = SkillDef(
  "default_attack",
  E.SectorTarget(
    target_type=TargetType.ENEMY,
    radius=2,
    children=[E.Damage(100)]
  )
)
