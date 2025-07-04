import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import swingable_primaries

quad_strike = SkillDef(
  "quad_strike",
  E.SectorTarget(
    target_type=TargetType.ENEMY,
    radius=2,
    max_targets=3,
    children=[E.Damage(70, hits=4)]
  ),
  mp_cost=30,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/quad_strike.png",
  rank=SkillRank.II,
  weapon_filter=lambda p, s: p in swingable_primaries
)
