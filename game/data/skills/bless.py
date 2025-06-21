from game.skills.effects import SelfTarget, ApplyBuff
from game.data.buffs import bless
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills import SkillRank

bless = SkillDef(
  SelfTarget(ApplyBuff(bless, 1, 10)),
  mp_cost=50,
  slot=SkillSlot.GAMMA,
  icon="assets/items/skills/bless.png",
  rank=SkillRank.II
)
