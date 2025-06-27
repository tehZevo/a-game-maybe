import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import swingable_primaries

#TODO: high sacrifice (30%)
sacrifice = SkillDef(
  "sacrifice",
  [
    E.SelfTarget(E.ConsumeHP(10)),
    E.SectorTarget(TargetType.ENEMY, angle=90, radius=3, children=[
      E.UserHPScaling(lambda hp: [E.Damage(hp * 100)])
    ])
  ],
  mp_cost=100,
  slot=SkillSlot.BETA,
  icon="assets/skills/sacrifice.png",
  rank=SkillRank.III,
  weapon_filter=lambda p, s: p in swingable_primaries
)
