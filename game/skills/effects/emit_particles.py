import game.components as C
from .skill_effect import SkillEffect
from game.utils import Vector

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self, skill):
    skill.entity.world.create_entity([
      #TODO: harcoded offset, need sprites to have origin at feet
      C.Position(skill.entity[C.Position].pos + Vector(0.5, 0.5)),
      C.ParticleEmitter("assets/particles/fire.png") #TODO: hardcoded particle
    ])
