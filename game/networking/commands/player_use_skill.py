from dataclasses import dataclass

from ..command_handler import CommandHandler
from game.actions import Move
from game.components.actor import Actor
from game.utils import find_entity_by_id, Vector
from game.items import SkillSlot

@dataclass
class PlayerUseSkill:
  slot: SkillSlot

  # def __dict__(self):
  #   return {"slot": slot.name}
  #
  # def __init__(self, slot):
  #   super().__init__()
  #   self.slot = SkillSlot[slot]

# a = PlayerUseSkill(SkillSlot.ALPHA)
# b = PlayerUseSkill("ALPHA")
# print(a)
# print(b)
# c

class PlayerUseSkillHandler(CommandHandler):
  def __init__(self, server_manager):
    super().__init__(PlayerUseSkill)
    self.server_manager = server_manager

  def handle(self, server, id, command):
    ent = find_entity_by_id(self.server_manager.entity.world, id)
    if ent is not None:
      ent.get_component(Actor).use_skill_in_slot(command.slot)
