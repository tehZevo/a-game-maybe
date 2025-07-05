from functools import reduce

#TODO: use some defaults instead of an explicit hands item?
from game.data.items import hands

from . import PrimaryStat, PrimaryStats, SecondaryStats, EquipStat, EquipStats

import game.components as C
from game.items.weapon_type import weapon_physical_stat_assignment, weapon_magical_stat_assignment
from game.items.slots import WeaponSlot
from .stats import Stats

#physical/magical attack are based on weapon attack and the weapon stats

PRIMARY_PATT_MULTIPLIER = 2
SECONDARY_PATT_MULTIPLIER = 1
PRIMARY_MATT_MULTIPLIER = 2
SECONDARY_MATT_MULTIPLIER = 1
VIT_PDEF_MULTIPLIER = 2
WIS_MDEF_MULTIPLIER = 2
DEX_ACC_MULTIPLIER = 20
AGI_EVA_MULTIPLIER = 20
AGI_MOVE_MULTIPLIER = 1
DEX_CRIT_MULTIPLIER = 1

BASE_EQUIP_STATS = EquipStats.One()
BASE_PRIMARY_STATS = PrimaryStats(10, 10, 10, 10, 10, 10)
BASE_SECONDARY_STATS = SecondaryStats(
  hp=50,
  mp=30,
  move_speed=100
)

def get_modifiers(entity):
  stats = entity.get_component(C.Stats)
  flat = stats.flat_modifiers.values()
  scaling = stats.scaling_modifiers.values()
  
  flat = reduce(lambda a, b: a + b, flat, Stats())
  scaling = reduce(lambda a, b: a + b, scaling, Stats.One)
  return flat, scaling
  
def calculate(entity):
  flat, scaling = get_modifiers(entity)
  stats_from_equips = get_stats_from_equips(entity)

  equip_stats = (BASE_EQUIP_STATS + stats_from_equips.equip + flat.equip) * scaling.equip

  primary_stats = (BASE_PRIMARY_STATS + stats_from_equips.primary + flat.primary) * scaling.primary
  
  base_secondary_stats = calculate_secondary_stats(entity, primary_stats, equip_stats)
  secondary_stats = (base_secondary_stats + stats_from_equips.secondary + flat.secondary) * scaling.secondary
  
  return Stats(
    primary=primary_stats,
    equip=equip_stats,
    secondary=secondary_stats,
  )

def get_stats_from_equips(entity):
  equips = entity.get_component(C.Equips)

  #sum up equip stats
  stats = Stats()

  for equip in equips.armor.values():
    if equip is not None:
      stats = stats + equip.stats

  for equip in equips.weapons.values():
    if equip is not None:
      stats = stats + equip.stats

  return stats

def calculate_secondary_stats(entity, primary_stats, equip_stats):
  #TODO: handle 2h and secondary weapons
  weapon = entity.get_component(C.Equips).weapons[WeaponSlot.PRIMARY]
  if weapon is None:
    weapon = hands

  return BASE_SECONDARY_STATS + SecondaryStats(
    hp=calculate_hp(primary_stats),
    mp=calculate_mp(primary_stats),
    phys_att=calculate_phys_attack(weapon, primary_stats, equip_stats),
    mag_att=calculate_mag_attack(weapon, primary_stats, equip_stats),
    phys_def=calculate_phys_def(weapon, primary_stats, equip_stats),
    mag_def=calculate_mag_def(weapon, primary_stats, equip_stats),
    accuracy=calculate_accuracy(primary_stats),
    evasion=calculate_evasion(primary_stats),
    move_speed=calculate_move_speed(primary_stats),
    critical=calculate_critical(primary_stats),
  )

def calculate_hp(primary_stats):
  return primary_stats.VIT ** 2

def calculate_mp(primary_stats):
  return primary_stats.WIS ** 2

def calculate_phys_attack(weapon, primary_stats, equip_stats):
  (phys_pri, phys_sec) = weapon_physical_stat_assignment(weapon)
  from_primary = primary_stats[phys_pri.name] * PRIMARY_PATT_MULTIPLIER
  from_secondary = primary_stats[phys_sec.name] * SECONDARY_PATT_MULTIPLIER
  return equip_stats.PATT * (from_primary + from_secondary)

def calculate_mag_attack(weapon, primary_stats, equip_stats):
  (mag_pri, mag_sec) = weapon_physical_stat_assignment(weapon)
  from_primary = primary_stats[mag_pri.name] * PRIMARY_MATT_MULTIPLIER
  from_secondary = primary_stats[mag_sec.name] * SECONDARY_MATT_MULTIPLIER
  return equip_stats.MATT * (from_primary + from_secondary)

def calculate_phys_def(weapon, primary_stats, equip_stats):
  return equip_stats.PDEF * primary_stats.VIT * VIT_PDEF_MULTIPLIER

def calculate_mag_def(weapon, primary_stats, equip_stats):
  return equip_stats.MDEF * primary_stats.WIS * WIS_MDEF_MULTIPLIER

def calculate_accuracy(primary_stats):
  return primary_stats.DEX * DEX_ACC_MULTIPLIER

def calculate_evasion(primary_stats):
  return primary_stats.AGI * AGI_EVA_MULTIPLIER

def calculate_move_speed(primary_stats):
  return primary_stats.AGI * AGI_MOVE_MULTIPLIER

def calculate_critical(primary_stats):
  return primary_stats.DEX * DEX_CRIT_MULTIPLIER
