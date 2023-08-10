from ..serde import Serde

class Event(Serde):
  def __init__(self):
    super().__init__()

  def handle(self, client):
    raise NotImplementedError
