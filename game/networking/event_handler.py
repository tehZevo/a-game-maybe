
class EventHandler:
  def __init__(self, event_type):
    self.event_type = event_type

  def handle(self, client, event):
    raise NotImplementedError
