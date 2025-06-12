from . import MobDef
from . import monster_archetypes as A
from game.items import Hat, SkillItem
from game.skills import test_alpha_skill, test_enemy_skill

slime = MobDef(
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[Hat(), SkillItem(test_alpha_skill), Hat(), SkillItem(test_alpha_skill), Hat(), SkillItem(test_alpha_skill), Hat(), SkillItem(test_alpha_skill), Hat(), SkillItem(test_alpha_skill)],
  skills=[test_alpha_skill],
  sprite="assets/slime.png"
)
