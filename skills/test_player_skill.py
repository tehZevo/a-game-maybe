from skilleffects import CircleTarget, Damage, Particles, Push
from components.enemy import Enemy

test_player_skill = CircleTarget(
  component_target=Enemy,
  radius=5,
  children=[
    Damage(100),
    Push(force=5000),
    Particles(),
  ]
)
