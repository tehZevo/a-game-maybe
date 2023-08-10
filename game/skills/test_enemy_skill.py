from skilleffects import CircleTarget, Damage, EmitParticles
from .skilldef import SkillDef
from skills.target_type import TargetType

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
