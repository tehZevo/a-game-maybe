from game.skilleffects import CircleTarget, Damage, EmitParticles
from . import TargetType, SkillDef

test_enemy_skill = SkillDef([
  CircleTarget(
    target_type=TargetType.ENEMY,
    radius=3,
    children=[
      Damage(75),
      EmitParticles(),
    ]
  )
], mp_cost=10, use_time=1)
