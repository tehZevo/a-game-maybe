from game.skills.effects import Damage, SelfTarget
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef

test_killme_skill = SkillDef([
  SelfTarget([Damage(99999999)]),
], mp_cost=0, slot=SkillSlot.OMEGA, icon=None)
