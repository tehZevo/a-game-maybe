from .event_handler import EventHandler

class RoomEventHandler(EventHandler):
  def __init__(self, event_type, game):
    super().__init__(event_type)
    self.game = game
