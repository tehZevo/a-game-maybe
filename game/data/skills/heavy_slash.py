import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import swingable_primaries

heavy_slash = SkillDef(
  "heavy_slash",
  [
    E.SectorTarget(
      target_type=TargetType.ENEMY,
      radius=2,
      children=[E.Damage(50)]
    ),
  ],
  mp_cost=15,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/heavy_slash.png",
  rank=SkillRank.I,
  weapon_filter=lambda p, s: p in swingable_primaries
)
