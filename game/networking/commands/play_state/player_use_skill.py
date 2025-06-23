from dataclasses import dataclass

from game.networking import PlayStateCommandHandler
from game.components.actor import Actor
from game.items.slots import SkillSlot

@dataclass
class PlayerUseSkill:
  slot: SkillSlot

class PlayerUseSkillHandler(PlayStateCommandHandler):
  def __init__(self, game_state):
    super().__init__(PlayerUseSkill, game_state)

  def handle(self, client_id, command):
    server_manager = self.game_state.server_manager
    entity_id = server_manager.player_entity_map[client_id]
    ent = server_manager.networked_entities[entity_id]
    ent.get_component(Actor).use_skill_in_slot(command.slot)
