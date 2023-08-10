from ecs import Component

class Team(Component):
  def __init__(self, team=None):
    super().__init__()
    self.team = team
