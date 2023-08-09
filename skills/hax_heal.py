from skilleffects import RestoreHealth, RestoreMana, SelfTarget
from skills.skilldef import SkillDef
from components.actor.enemy import Enemy

hax_heal = SkillDef([
  SelfTarget([RestoreHealth(), RestoreMana()])
])
