from game.skills.effects import CircleTarget, Damage, EmitParticles, Push, Rush, SelfTarget
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills.target_type import TargetType
from game.skills import SkillRank

dev_rush = SkillDef(
  "dev_rush",
  [
    SelfTarget(Rush(force=5000)),
    CircleTarget(
      target_type=TargetType.ENEMY,
      radius=5,
      children=[
        Damage(100),
        Push(force=5000),
        EmitParticles(),
      ]
    )
  ],
  mp_cost=10,
  slot=SkillSlot.ALPHA,
  icon="assets/items/skills/dev_rush.png",
  mini_icon="assets/icons/dev.png",
  rank=SkillRank.IV,
  use_time=0.5
)
