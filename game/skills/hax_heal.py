from game.skills.skilldef import SkillDef
from game.skilleffects import RestoreHealth, RestoreMana, SelfTarget

hax_heal = SkillDef([
  SelfTarget([RestoreHealth(), RestoreMana()])
])
