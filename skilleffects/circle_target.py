from skilleffects import Target
from skilleffects.target_filters import distance_filter, target_type_filter

class CircleTarget(Target):
  def __init__(self, target_type, radius=2, children=[]):
    super().__init__([
      distance_filter(radius),
      target_type_filter(target_type)
    ], children=children)
