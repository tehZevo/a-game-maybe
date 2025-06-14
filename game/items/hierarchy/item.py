from game.items.rarity import Rarity, base_drop_rate

class Item:
  def __init__(self, id=None, rarity=None, icon=None, mod_drop_rate=None):
    super().__init__()
    self.id = id
    self.icon = icon or "assets/unknown.png"
    self.rarity = Rarity.COMMON if rarity is None else rarity
    self.mod_drop_rate = 1 if mod_drop_rate is None else mod_drop_rate

  def calc_drop_rate(self):
    return base_drop_rate(self.rarity) * self.mod_drop_rate