from game.items.defs import Weapon
from game.stats import EquipStats, PrimaryStats, Stats

#monster weapons ironically contain both defensive and offensive stats
def create_monster_weapon(base=10, archetypes=[]):
  equip = EquipStats(base, base, base, base)
  primary = PrimaryStats(base, base, base, base, base, base)
  for archetype in archetypes:
    equip, primary = archetype(equip, primary)
  return Weapon(stats=Stats(equip=equip, primary=primary))
