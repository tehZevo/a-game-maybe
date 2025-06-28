from .target import Target

class SelfTarget(Target):
  def __init__(self, children=[]):
    super().__init__([
      lambda skill: lambda actor: actor == skill.user
    ], children=children)
