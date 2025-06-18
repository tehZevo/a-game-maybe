from game.buffs import BuffEffect
from game.utils.constants import DOT_TICK_RATE, DT
import game.components as C

class HealOverTime(BuffEffect):
    def __init__(self, amount_per_power=1):
        super().__init__()
        self.amount_per_power = amount_per_power
    
    def apply(self, buff):
        return 0 #our state (time since last tick)
    
    def update(self, buff, time_since_last_tick):
        time_since_last_tick += DT
        while time_since_last_tick >= DOT_TICK_RATE:
            actor = buff.target.get_component(C.Actor)
            actor.heal(self.amount_per_power * buff.power)
            time_since_last_tick -= DOT_TICK_RATE
        return time_since_last_tick
