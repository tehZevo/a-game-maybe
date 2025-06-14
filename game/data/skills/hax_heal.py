from game.skills.skilldef import SkillDef
from game.items.slots import SkillSlot
from game.skills.effects import RestoreHealth, RestoreMana, SelfTarget

hax_heal = SkillDef([
  SelfTarget([RestoreHealth(), RestoreMana()])
], slot=SkillSlot.BETA, icon=None)
