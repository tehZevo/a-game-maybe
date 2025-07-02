import game.skills.effects as E
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank
from game.items.weapon_type import can_cast_magic_primaries
import game.data.sprites as S

fireball = SkillDef(
  "fireball",
  E.Projectile(TargetType.ENEMY, S.fireball, on_tick=[E.Damage(100)], radius=2, life=0.5, max_targets=6, speed=8),
  mp_cost=30,
  slot=SkillSlot.ALPHA,
  icon="assets/skills/fireball.png",
  rank=SkillRank.II,
  weapon_filter=lambda p, s: p in can_cast_magic_primaries
)
