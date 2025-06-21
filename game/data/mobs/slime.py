from game.monsters import MobDef
import game.monsters.monster_archetypes as A
from game.data.skills import test_enemy_skill
import game.data.items as I
import game.data.sprites as S

slime = MobDef(
  id="slime",
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[I.cloth_hat, I.bless, I.wooden_longsword, I.wooden_shortsword, I.wooden_shortsword_l, I.wooden_shield],
  skills=[test_enemy_skill],
  sprite=S.slime
)
