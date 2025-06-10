from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Interact
from game.components.actor import Actor

@dataclass
class PlayerInteract:
  pass

class PlayerInteractHandler(CommandHandler):
  def __init__(self):
    super().__init__(PlayerInteract)

  def handle(self, server_manager, server, client_id, command):
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(Actor).act(Interact())
