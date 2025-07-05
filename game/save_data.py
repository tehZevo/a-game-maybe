import game.components as C

class SaveData:
  def __init__(self):
    self.player_data = {}
  
  def save_player_data(self, client_id, player):
    pd = {}
    equips = player[C.Equips]
    pd["equips"] = equips.save()
    self.player_data[client_id] = pd
  
  def load_player_data(self, client_id, player):
    pd = self.player_data[client_id]
    player[C.Equips].load(pd["equips"])
    player[C.Stats].recalculate()
    