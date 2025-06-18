from game.buffs import BuffDef
from game.buffs.effects import HealOverTime

heal_over_time_buff = BuffDef("heal_over_time_buff", [
    HealOverTime(10)
], icon="assets/buffs/heal_over_time.png")