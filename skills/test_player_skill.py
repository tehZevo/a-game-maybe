from skilleffects import CircleTarget, Damage, Particles
from components.enemy import Enemy

test_player_skill = CircleTarget(
  component_target=Enemy,
  radius=5,
  children=[
    Damage(300),
    Particles(),
  ]
)
