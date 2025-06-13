from . import MobDef
from . import monster_archetypes as A
from game.skills import test_enemy_skill
from game.items.registry import cloth_hat, test_alpha_skill_item

slime = MobDef(
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[cloth_hat, test_alpha_skill_item, cloth_hat, test_alpha_skill_item, cloth_hat, test_alpha_skill_item, cloth_hat, test_alpha_skill_item, cloth_hat, test_alpha_skill_item],
  skills=[test_enemy_skill],
  sprite="assets/slime.png"
)
