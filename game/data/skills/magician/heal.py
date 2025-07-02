import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import can_cast_magic_primaries
import game.data.sprites as S

heal = SkillDef(
  "heal",
  E.CircleTarget(TargetType.ALLY, radius=4, max_targets=4, children=[
    E.Heal(100)
  ]),
  mp_cost=20,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/heal.png",
  rank=SkillRank.II,
  weapon_filter=lambda p, s: p in can_cast_magic_primaries
)
