import game.networking.events as E

from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from .buffs_listener import BuffsListener
import game.components as C

class BuffsSyncing(Component, NetworkBehavior, BuffsListener):
  def __init__(self):
    super().__init__()
    self.require(C.Buffs, C.Networking)

  def to_client_buff(self, buff):
    return E.ClientBuff(buff.id, buff.power, buff.initial_time, buff.time)
    
  def on_buffs_changed(self, buffs):
    networking = self.get_component(C.Networking)
    if not networking.is_server:
      return
    
    buffs = [E.ClientBuff(b.buffdef.id, b.power, b.initial_time, b.time) for b in buffs.values()]
    evt = E.BuffsUpdated(networking.id, buffs)
    networking.broadcast_synced(evt)
