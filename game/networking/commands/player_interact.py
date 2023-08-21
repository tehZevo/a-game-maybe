from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Interact
from game.components.actor import Actor

@dataclass
class PlayerInteract:
  pass

class PlayerInteractHandler(CommandHandler):
  def __init__(self, server_manager):
    super().__init__(PlayerInteract)
    self.server_manager = server_manager

  def handle(self, server, id, command):
    ent = self.server_manager.networked_entities[id]
    if ent is not None:
      ent.get_component(Actor).act(Interact())
