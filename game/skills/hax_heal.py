from skilleffects import RestoreHealth, RestoreMana, SelfTarget
from skills.skilldef import SkillDef

hax_heal = SkillDef([
  SelfTarget([RestoreHealth(), RestoreMana()])
])
