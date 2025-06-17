import time
from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.networking.events import Pong

@dataclass
class Ping:
  time: float

class PingHandler(CommandHandler):
  def __init__(self):
    super().__init__(Ping)

  def handle(self, server_manager, server, client_id, command):
    dt = time.time() - command.time
    print("[Server] Ping! Took", dt, "seconds.")
    server.send(client_id, Pong(command.time))
