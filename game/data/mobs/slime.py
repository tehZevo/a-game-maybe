from game.monsters import MobDef
import game.monsters.monster_archetypes as A
from game.data.skills import test_enemy_skill
import game.data.items as I

slime = MobDef(
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[I.cloth_hat, I.test_alpha_skill_item],
  skills=[test_enemy_skill],
  sprite="assets/slime.png"
)
