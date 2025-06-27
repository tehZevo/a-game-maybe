from game.skills.skilldef import SkillDef
from game.items.slots import SkillSlot
from game.skills.effects import RestoreHealth, RestoreMana, SelfTarget
from game.skills import SkillRank

dev_heal = SkillDef(
  "dev_heal",
  SelfTarget([
    RestoreHealth(),
    RestoreMana()
  ]),
  slot=SkillSlot.BETA,
  icon="assets/skills/dev_heal.png",
  mini_icon="assets/icons/dev.png",
  rank=SkillRank.IV
)
