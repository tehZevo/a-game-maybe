from ecs import Component

class GameMaster(Component):
  def __init__(self, game):
    super().__init__()
    self.game = game
