from dataclasses import dataclass
from typing import List

from ..event_handler import EventHandler
import game.components as C
from game.data.registry import get_buff
from game.constants import DT

@dataclass
class ClientBuff:
  buffdef_id: str
  power: float
  initial_time: float
  time: float
  
  def __init__(self, buffdef_id, power, initial_time, time):
    self.buffdef_id = buffdef_id
    self.buffdef = get_buff(buffdef_id)
    self.power = power
    self.initial_time = initial_time
    self.time = time
  
  def update(self):
    self.time -= DT
    self.time = max(0, self.time)

@dataclass
class BuffsUpdated:
  id: str
  buffs: List[ClientBuff]

class BuffsUpdatedHandler(EventHandler):
  def __init__(self):
    super().__init__(BuffsUpdated)

  def handle(self, client_manager, client, event):
    ent = client_manager.networked_entities.get(event.id)

    if ent is None:
      return
    
    buffs = ent.ensure_component(C.ClientBuffs)
    buffs.set_buffs(event.buffs)
