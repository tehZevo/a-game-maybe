from skilleffects import CircleTarget, Damage, EmitParticles
from .skilldef import SkillDef
from components.actor.player import Player

test_enemy_skill = SkillDef([
  CircleTarget(
    component_target=Player,
    radius=3,
    children=[
      Damage(75),
      EmitParticles(),
    ]
  )
], mp_cost=10, use_time=1)
