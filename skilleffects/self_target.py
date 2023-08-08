from skilleffects import Target

class SelfTarget(Target):
  def __init__(self, children=[]):
    super().__init__([
      lambda _, actor: actor == self.user
    ], children=children)
