import game.skills.effects as E
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType

slash = SkillDef(
  "slash",
  [
    E.SectorTarget(
      target_type=TargetType.ENEMY,
      radius=2,
      children=[E.Damage(10)]
    ),
  ],
  slot=None,
  icon=None
)
