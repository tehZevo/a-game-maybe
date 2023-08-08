from skilleffects import CircleTarget, Damage, EmitParticles
from components.actor.player import Player

test_enemy_skill = CircleTarget(
  component_target=Player,
  radius=3,
  children=[
    Damage(0),
    EmitParticles(),
  ]
)
