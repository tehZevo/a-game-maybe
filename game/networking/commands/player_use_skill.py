from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.components.actor import Actor
from game.items.slots import SkillSlot

@dataclass
class PlayerUseSkill:
  slot: SkillSlot

class PlayerUseSkillHandler(CommandHandler):
  def __init__(self):
    super().__init__(PlayerUseSkill)

  def handle(self, server_manager, server, client_id, command):
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(Actor).use_skill_in_slot(command.slot)
