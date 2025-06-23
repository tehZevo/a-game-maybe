from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
from game.actions import Interact
from game.components.actor import Actor

@dataclass
class PlayerInteract:
  pass

class PlayerInteractHandler(PlayStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(PlayerInteract, game_state)

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(Actor).act(Interact())
