from . import MobDef
from . import monster_archetypes as A

slime = MobDef(
  difficulty=5,
  archetypes=[A.MOOK],
  sprite="assets/slime.png"
)
