from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Move
from game.utils import find_entity_by_id, Vector

@dataclass
class PlayerMove:
  dir: Vector

class PlayerMoveHandler(CommandHandler):
  def __init__(self, server_manager):
    super().__init__(PlayerMove)
    self.server_manager = server_manager

  def handle(self, server, id, command):
    ent = find_entity_by_id(self.server_manager.entity.world, id)
    if ent is not None:
      ent.get_component.actor.act(Move(command.dir))
