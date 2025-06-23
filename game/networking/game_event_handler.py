
class GameEventHandler:
  def __init__(self, event_type, game):
    self.event_type = event_type
    self.game = game

  def handle(self, event):
    raise NotImplementedError
