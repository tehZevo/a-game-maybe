from game.components.particles import ParticleEmitter
from game.components.physics import Position
from . import SkillEffect

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    #TODO: hardcoded particles
    self.entity.world.create_entity([
      Position(self.entity.get_component(Position).pos),
      ParticleEmitter("assets/particles/spark.png")
    ])
