from skilleffects import CircleTarget, Damage, EmitParticles, Push, Rush, SelfTarget
from .skilldef import SkillDef
from components.actor.enemy import Enemy

test_player_skill = SkillDef([
  SelfTarget([Rush(force=5000)]),
  CircleTarget(
    component_target=Enemy,
    radius=5,
    children=[
      Damage(100),
      Push(force=5000),
      EmitParticles(),
    ]
  )
], mp_cost=10, use_time=0.25)
