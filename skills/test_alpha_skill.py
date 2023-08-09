from skilleffects import CircleTarget, Damage, EmitParticles, Push, Rush, SelfTarget
from .skilldef import SkillDef
from .target_type import TargetType
from items.slots import SkillSlot

test_alpha_skill = SkillDef([
  SelfTarget([Rush(force=5000)]),
  CircleTarget(
    target_type=TargetType.ENEMY,
    radius=5,
    children=[
      Damage(100),
      Push(force=5000),
      EmitParticles(),
    ]
  )
], mp_cost=10, slot=SkillSlot.ALPHA, icon="assets/items/skills/alpha.png")
