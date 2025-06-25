from dataclasses import dataclass

from game.networking import LobbyStateEventHandler

#TODO: send this when players join/leave lobby
@dataclass
class LobbyUpdated:
  ready_players: set

class LobbyUpdatedHandler(LobbyStateEventHandler):
  def __init__(self, game_state):
    super().__init__(LobbyUpdated, game_state)

  def handle(self, event):
    self.game_state.ready = event.ready_players