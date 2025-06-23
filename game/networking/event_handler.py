
class EventHandler:
  def __init__(self, event_type):
    self.event_type = event_type

  #TODO: remove either client_manager or client...
  def handle(self, event):
    raise NotImplementedError
