import game.components as C
from .skill_effect import SkillEffect

class EmitParticles(SkillEffect):
  def __init__(self):
    super().__init__()

  def start(self, skill):
    pass
    #TODO: was generating lag because server never cleaned up emitters - fix first
    # skill.entity.world.create_entity([
    #   C.Position(skill.entity.get_component(C.Position).pos),
    #   C.ParticleEmitter("assets/particles/spark.png")
    # ])
