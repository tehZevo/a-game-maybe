from game.components.particles import ParticleEmitter
from game.components import physics
from . import SkillEffect

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    #TODO: hardcoded particles
    self.entity.world.create_entity([
      physics.Position(self.entity.get_component(physics.Position).pos),
      ParticleEmitter("assets/particles/spark.png")
    ])
