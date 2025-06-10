from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Move
from game.components.actor import Actor
from game.utils import Vector

@dataclass
class PlayerMove:
  dir: Vector

class PlayerMoveHandler(CommandHandler):
  def __init__(self):
    super().__init__(PlayerMove)

  def handle(self, server_manager, server, client_id, command):
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(Actor).act(Move(command.dir))
