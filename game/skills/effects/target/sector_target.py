from game.skills.target_filters import distance_filter, target_type_filter, angle_filter
from .target import Target

class SectorTarget(Target):
  def __init__(self, target_type, angle=360, radius=2, max_targets=1, children=[]):
    super().__init__([
      distance_filter(radius),
      target_type_filter(target_type),
      angle_filter(angle)
    ], max_targets=max_targets, children=children)
