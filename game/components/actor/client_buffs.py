from game.ecs import Component
from game.buffs import Buff

#TODO: i dont like this paradigm but it simplifies how to sync buffs
class ClientBuffs(Component):
  def __init__(self):
    super().__init__()
    self.buffs = []

  def set_buffs(self, buffs):
    self.buffs = buffs

  def update(self):
    for buff in self.buffs:
      buff.update()