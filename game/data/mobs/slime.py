from game.monsters import MobDef
import game.monsters.monster_archetypes as A
from game.data.skills import test_enemy_skill
import game.data.items as I
import game.data.sprites as S

slime = MobDef(
  id="slime",
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[
    I.cotton_hat, I.cotton_robe, I.cotton_gloves, I.cotton_shoes,
    I.wooden_shield, I.bless
  ],
  skills=[test_enemy_skill],
  sprite=S.slime
)
