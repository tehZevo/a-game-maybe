import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import can_cast_magic_primaries
import game.data.sprites as S

magic_bolt = SkillDef(
  "magic_bolt",
  E.Projectile(TargetType.ENEMY, S.magic_bolt, on_tick=[E.Damage(80)], life=0.5, speed=8, max_targets=3),
  mp_cost=20,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/magic_bolt.png",
  rank=SkillRank.I,
  weapon_filter=lambda p, s: p in can_cast_magic_primaries
)
