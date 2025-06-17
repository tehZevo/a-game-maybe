import time
from dataclasses import dataclass

from ..event_handler import EventHandler

@dataclass
class Pong:
  time: float

class PongHandler(EventHandler):
  def __init__(self):
    super().__init__(Pong)

  def handle(self, client_manager, client, event):
    dt = time.time() - event.time
    print("[Client] Pong! Took", dt, "seconds.")
