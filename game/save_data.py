from .components.actor.player import Player
from .components.item.equips import Equips

class SaveData:
  def __init__(self):
    self.player_data = {}
  
  def save_player_data(self, client_id, player):
    pd = {}
    equips = player.get_component(Equips)
    pd["equips"] = equips.save()
    self.player_data[client_id] = pd
  
  def load_player_data(self, client_id, player):
    pd = self.player_data[client_id]
    player.get_component(Equips).load(pd["equips"])
    