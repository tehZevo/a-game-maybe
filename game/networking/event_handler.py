
class EventHandler:
  def __init__(self, event_type):
    self.event_type = event_type

  def handle(server, id, command):
    raise NotImplementedError
