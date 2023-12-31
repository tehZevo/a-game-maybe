from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.components.actor import Actor
from game.items import SkillSlot

@dataclass
class PlayerUseSkill:
  slot: SkillSlot

class PlayerUseSkillHandler(CommandHandler):
  def __init__(self, server_manager):
    super().__init__(PlayerUseSkill)
    self.server_manager = server_manager

  def handle(self, server, id, command):
    ent = self.server_manager.networked_entities[id]
    if ent is not None:
      ent.get_component(Actor).use_skill_in_slot(command.slot)
