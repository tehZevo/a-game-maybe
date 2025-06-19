import game.components as C
from .skill_effect import SkillEffect

#push effect pushes away from a given point
#can also be used as a pull by using a negative force
class Push(SkillEffect):
  def __init__(self, force=1, scale_with_distance=True):
    super().__init__()
    self.force = force
    self.scale_with_distance = scale_with_distance

  def start(self, skill):
    #calc dist and direction, source location is parent skill effect
    effect_pos = skill.parent.get_component(C.Position).pos
    target_pos = skill.target.get_component(C.Position).pos
    dist = effect_pos.distance(target_pos)
    dir = (target_pos - effect_pos).normalized()

    #scale force with distance
    force = self.force
    if self.scale_with_distance:
      force = force / max(1, dist) #max with 1 to prevent low dist from sending enemies into LEO

    skill.target.get_component(C.Physics).apply_force(dir * force)
