import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import swingable_primaries

sanguine_strike = SkillDef(
  "sanguine_strike",
  E.SectorTarget(TargetType.ENEMY, angle=180, radius=2, children=[
    E.Damage(100),
    E.StealHP(100)
  ]),
  mp_cost=40,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/sanguine_strike.png",
  rank=SkillRank.II,
  weapon_filter=lambda p, s: p in swingable_primaries
)
