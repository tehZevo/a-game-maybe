from skills import SkillEffect
from components.particles.particle_emitter import ParticleEmitter
from components.position import Position

#TODO: rename to emitparticles
class Particles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    #TODO: hardcoded particles
    self.entity.world.create_entity([
      Position(self.entity.get_component(Position).pos),
      ParticleEmitter("assets/particles/spark.png")
    ])
