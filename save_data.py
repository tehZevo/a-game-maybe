from components.actor.player import Player
from components.item.equips import Equips

class SaveData:
  def __init__(self, world):
    #TODO: handle multiple players
    players = world.find(Player)
    equips_comp = players[0].get_component(Equips)
    #grab equips
    self.equips = {k: equips_comp.__dict__[k] for k in equips_comp.save()}

  def apply(self, world):
    #TODO: handle multiple players
    players = world.find(Player)
    #rehydrate equips
    players[0].get_component(Equips).load(self.equips)
