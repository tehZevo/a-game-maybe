from game.skills.target_filters import distance_filter, target_type_filter
from .target import Target

class CircleTarget(Target):
  def __init__(self, target_type, radius=2, max_targets=1, children=[]):
    super().__init__([
      distance_filter(radius),
      target_type_filter(target_type)
    ], max_targets=max_targets, children=children)
