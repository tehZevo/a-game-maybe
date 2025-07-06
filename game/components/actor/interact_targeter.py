from game.ecs import Component
import game.components as C
from game.components.networking import NetworkBehavior
from game.utils.find_in_range import find_in_range
from game.constants import DT, INTERACT_RADIUS, INTERACT_TARGET_UPDATE_TIME, INTERACT_TARGET_DISTANCE
import game.networking.events as E

class InteractTargeter(Component, NetworkBehavior):
  def __init__(self):
    super().__init__()
    self.require(C.Actor, C.Position)
    self.interact_target = None
    self.time_since_last_update = 0

  def send_update_to_player(self, networking, pos):
    if self.entity[C.Player] is None:
      return
    
    event = E.InteractTargetUpdated(pos)
    client_id = networking.server_manager.find_player_by_entity_id(networking.id)
    networking.send_to_client(client_id, event)

  def update_server(self, networking):
    self.time_since_last_update += DT

    if self.interact_target is not None and not self.interact_target.alive:
      self.interact_target = None
      self.send_update_to_player(networking, None)

    if self.time_since_last_update < INTERACT_TARGET_UPDATE_TIME:
      return
    
    self.time_since_last_update = 0
    my_pos = self.entity[C.Position].pos
    look_dir = self.entity[C.Actor].look_dir
    interact_center_pos = my_pos + look_dir * INTERACT_TARGET_DISTANCE

    interactables = find_in_range(self.entity.world, C.Interactable, interact_center_pos, INTERACT_RADIUS, sort=True)
    new_target = None if len(interactables) == 0 else interactables[0]

    if new_target == self.interact_target:
      return
    
    self.interact_target = new_target
    target_pos = new_target and new_target[C.Position].pos
    self.send_update_to_player(networking, target_pos)