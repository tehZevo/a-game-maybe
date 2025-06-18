from game.skills.effects import SelfTarget, ApplyBuff
from game.data.buffs import bless
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef

test_buff_skill = SkillDef([
  SelfTarget([
    ApplyBuff(bless, 1, 10)
  ]),
], mp_cost=0, slot=SkillSlot.GAMMA, icon=None)
