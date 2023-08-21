from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Move
from game.components.actor import Actor
from game.utils import Vector

@dataclass
class PlayerMove:
  dir: Vector

class PlayerMoveHandler(CommandHandler):
  def __init__(self, server_manager):
    super().__init__(PlayerMove)
    self.server_manager = server_manager

  def handle(self, server, id, command):
    ent = self.server_manager.networked_entities[id]
    if ent is not None:
      ent.get_component(Actor).act(Move(command.dir))
