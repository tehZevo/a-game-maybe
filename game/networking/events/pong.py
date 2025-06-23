import time
from dataclasses import dataclass

from game.networking import GameEventHandler

@dataclass
class Pong:
  time: float

class PongHandler(GameEventHandler):
  def __init__(self, game):
    super().__init__(Pong, game)

  def handle(self, event):
    dt = time.time() - event.time
    print("[Client] Pong! Took", dt, "seconds.")
