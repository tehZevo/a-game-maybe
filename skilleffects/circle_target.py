from skilleffects import Target
from skilleffects.target_filters import distance_filter, component_filter

class CircleTarget(Target):
  def __init__(self, component_target, radius=2, children=[]):
    super().__init__([
      distance_filter(radius),
      component_filter(component_target)
    ], children=children)
