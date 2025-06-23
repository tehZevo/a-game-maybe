import time
from dataclasses import dataclass

from ..game_command_handler import GameCommandHandler
import game.networking.events as E

@dataclass
class Ping:
  time: float

class PingHandler(GameCommandHandler):
  def __init__(self, game):
    super().__init__(Ping, game)

  def handle(self, client_id, command):
    dt = time.time() - command.time
    print("[Server] Ping! Took", dt, "seconds.")
    self.game.server.default_channel.send(client_id, E.Pong(command.time))
