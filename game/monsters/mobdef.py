#TODO: different equip sets for different difficulty of monster
#TODO: different mob def templates

class MobDef:
  def __init__(self, drops=[], armor=[], skills=[], weapons=[], sprite=None):
    self.drops = drops
    self.armor = armor
    self.skills = skills
    self.weapons = weapons
    self.sprite = sprite
