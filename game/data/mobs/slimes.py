from game.monsters import MobDef
import game.monsters.monster_archetypes as A
from game.data.skills import test_enemy_skill
import game.data.items as I
import game.data.sprites as S

def make_slime(id, sprite, drops):
  return MobDef(
    id=id,
    difficulty=5,
    archetypes=[A.MOOK],
    drops=drops,
    skills=[test_enemy_skill],
    sprite=sprite
  )

slime = MobDef(
  id="slime",
  difficulty=5,
  archetypes=[A.MOOK],
  drops=[
    I.cotton_hat, I.cotton_robe, I.cotton_gloves, I.cotton_shoes,
    I.wooden_shield
  ],
  skills=[test_enemy_skill],
  sprite=S.slime
)

green_slime = MobDef(
  id="green_slime",
  sprite=S.green_slime,
  drops=[
    I.linen_hat, I.linen_robe, I.linen_gloves, I.linen_shoes,
    I.bless
  ]
)

brown_slime = MobDef(
  id="brown_slime",
  sprite=S.brown_slime,
  drops=[
    I.wooden_helmet, I.wooden_suit, I.wooden_gloves, I.wooden_boots,
    I.wooden_shortsword, I.wooden_longsword, I.wooden_shield
  ]
)

red_slime = MobDef(
  id="red_slime",
  sprite=S.red_slime,
  drops=[
    I.copper_helmet, I.copper_suit, I.copper_gloves, I.copper_boots,
    I.copper_shortsword, I.copper_longsword, I.copper_shield
  ]
)

dark_slime = MobDef(
  id="dark_slime",
  sprite=S.dark_slime,
  drops=[
    I.leather_hat, I.leather_suit, I.leather_gloves, I.leather_shoes
  ]
)

pink_slime = MobDef(
  id="dark_slime",
  sprite=S.dark_slime,
  drops=[
    I.hide_hat, I.hide_suit, I.hide_gloves, I.hide_shoes
  ]
)