from skilleffects import SkillEffect
from components.particles.particle_emitter import ParticleEmitter
from components.physics.position import Position

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    #TODO: hardcoded particles
    self.entity.world.create_entity([
      Position(self.entity.get_component(Position).pos),
      ParticleEmitter("assets/particles/spark.png")
    ])
