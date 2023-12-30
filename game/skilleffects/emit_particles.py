from game.components.particles import ParticleEmitter
import game.components as C
from . import SkillEffect

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    #TODO: hardcoded particles
    self.entity.world.create_entity([
      C.Position(self.entity.get_component(C.Position).pos),
      ParticleEmitter("assets/particles/spark.png")
    ])
