import game.skills.effects as E
from game.data.buffs import heal_over_time_buff
from game.items.slots import SkillSlot
from game.skills.skilldef import SkillDef
from game.skills import SkillRank

heal_burst = SkillDef(
  "heal_burst",
  [
    E.SelfTarget(E.ApplyBuff(heal_over_time_buff, 1, 10)),
    E.EmitParticles()
  ],
  mp_cost=50,
  cooldown=5,
  slot=SkillSlot.GAMMA,
  icon="assets/skills/heal_burst.png",
  rank=SkillRank.II
)