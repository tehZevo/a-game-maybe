from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
import game.actions as A
import game.components as C

@dataclass
class PlayerAttack:
  pass

class PlayerAttackHandler(PlayStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(PlayerAttack, game_state)

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(C.Actor).act(A.Attack())
