from skilleffects import CircleTarget, Damage, EmitParticles, Push, Rush, SelfTarget
from components.actor.enemy import Enemy

test_player_skill = [
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
]
