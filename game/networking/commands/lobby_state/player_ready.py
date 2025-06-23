from dataclasses import dataclass

from game.networking import LobbyStateCommandHandler

@dataclass
class PlayerReady:
  pass

class PlayerReadyHandler(LobbyStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(PlayerReady, game_state)

  def handle(self, client_id, command):
    #TODO: toggle or add flag to command
    ready = True
    print("[Server] Player", client_id, "ready:", ready)
    self.game_state.set_player_ready(client_id, ready)
