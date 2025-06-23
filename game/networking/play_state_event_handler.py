from .event_handler import EventHandler

class PlayStateEventHandler(EventHandler):
  def __init__(self, event_type, game_state):
    super().__init__(event_type)
    self.game_state = game_state
