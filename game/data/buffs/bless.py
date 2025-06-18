from game.buffs import BuffDef
import game.buffs.effects as E
from game.stats import Stats
from game.data.buffs import heal_over_time_buff

bless = BuffDef("bless", [
    E.ModifyStats(Stats.Primary(VIT=20, WIS=20)),
    E.ChildBuff(heal_over_time_buff)
], icon="assets/buffs/bless.png")