from game.items.monster_items import create_monster_weapon

#TODO: different equip sets for different difficulty of monster
#TODO: different mob def templates

class MobDef:
  def __init__(self, difficulty=10, archetypes=[], drops=[], skills=[], sprite=None):
    self.weapon = create_monster_weapon(difficulty, archetypes)
    self.drops = drops
    self.skills = skills
    self.sprite = sprite
