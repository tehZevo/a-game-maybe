from .event import Event

class TestEvent(Event):
  def __init__(self):
    super().__init__()

  def handle(self, client):
    print("hello world!")
