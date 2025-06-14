from game.components.particles import ParticleEmitter
import game.components as C
from .skill_effect import SkillEffect

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self):
    pass
    #TODO: was generating lag because server never cleaned up emitters - fix first
    # self.entity.world.create_entity([
    #   C.Position(self.entity.get_component(C.Position).pos),
    #   ParticleEmitter("assets/particles/spark.png")
    # ])
