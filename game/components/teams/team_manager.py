from collections import defaultdict

from game.ecs import Component
from game.utils.teams import Disposition

#:^)
def make_key(a, b):
  return tuple(sorted([a, b]))

#stores order-invariant mappings of pairs of teams to their dispositions
class TeamManager(Component):
  def __init__(self, team=None):
    super().__init__()
    self.team = team
    self.dispositions = defaultdict(lambda: Disposition.NEUTRAL)

  def set_disposition(self, a, b, disposition):
    if a is None or b is None or disposition is None:
      raise ValueError(f"Both teams and disposition must be non-none, received: {a}, {b}, {disposition}")

    self.dispositions[make_key(a, b)] = disposition

  def get_disposition(self, a, b):
    return self.dispositions[make_key(a, b)]
