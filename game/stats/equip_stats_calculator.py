from game.stats import Stats, PrimaryStats, EquipStats

plate_str = PrimaryStats(2, 1, 0, 0, 0, 0)
plate_vit = PrimaryStats(1, 2, 0, 0, 0, 0)

light_dex = PrimaryStats(0, 0, 2, 1, 0, 0)
light_agi = PrimaryStats(0, 0, 1, 2, 0, 0)

cloth_int = PrimaryStats(0, 0, 0, 0, 2, 1)
cloth_wis = PrimaryStats(0, 0, 0, 0, 1, 2)

plate = EquipStats(0, 0, 2, 0)
light = EquipStats(0, 0, 1, 0)
cloth = EquipStats(0, 0, 0, 2)

def part_multiplier(equip_class):
  import game.items as I

  if issubclass(equip_class, I.Weapon):
    return 0.2
  
  #TODO: may have to use issubclass for other types here too eventually
  match equip_class:
    case I.Suit: return 0.4
    case I.Hat: return 0.1
    case I.Gloves: return 0.1
    case I.Shoes: return 0.1
  return 0

def grade_multiplier(grade):
  from game.items import EquipGrade as G
  match grade:
    case G.E: return 10
    case G.D: return 20
    case G.C: return 30
    case G.B: return 40
    case G.A: return 60
    case G.S: return 80
    case G.SS: return 100
  return 10

def calc_primary_archetype_stats(archetype, equip_class, grade):
  primary = archetype * grade_multiplier(grade) * part_multiplier(equip_class)
  return Stats(primary=primary)