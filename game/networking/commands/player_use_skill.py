from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.components.actor import Actor
from game.items import SkillSlot

@dataclass
class PlayerUseSkill:
  slot: SkillSlot

class PlayerUseSkillHandler(CommandHandler):
  def __init__(self):
    super().__init__(PlayerUseSkill)

  def handle(self, server_manager, server, id, command):
    ent = server_manager.networked_entities[id]
    if ent is not None:
      ent.get_component(Actor).use_skill_in_slot(command.slot)
