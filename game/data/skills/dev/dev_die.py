from game.skills.effects import Damage, SelfTarget
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills import SkillRank

dev_die = SkillDef(
  "dev_die",
  SelfTarget(Damage(99999999)),
  slot=SkillSlot.OMEGA,
  icon="assets/skills/dev_die.png",
  mini_icon="assets/icons/dev.png",
  rank=SkillRank.IV
)
