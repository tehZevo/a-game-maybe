from game.constants import DT

#an instance of a buffdef, with state for each effect
class Buff:
    def __init__(self, buffdef, power, time, target, caster):
        self.buffdef = buffdef
        self.power = power
        self.initial_time = time
        self.time = time
        self.caster = caster
        self.target = target
        self.effect_states = None
    
    def apply(self):
        states = []
        for effect in self.buffdef.effects:
            states.append(effect.apply(self))
        self.effect_states = states
    
    def update(self):
        self.time -= DT
        new_states = []
        for effect, state in zip(self.buffdef.effects, self.effect_states):
            new_states.append(effect.update(self, state))
        self.effect_states = new_states
    
    def remove(self):
        for effect, state in zip(self.buffdef.effects, self.effect_states):
            effect.remove(self, state)