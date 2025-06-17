from game.skills.effects import SelfTarget, ApplyBuff
from game.data.buffs import heal_over_time_buff
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef

test_buff_skill = SkillDef([
  SelfTarget([
    ApplyBuff(heal_over_time_buff, 1, 10)
  ]),
], mp_cost=0, slot=SkillSlot.GAMMA, icon=None)
