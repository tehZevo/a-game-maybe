from functools import reduce

#TODO: use some defaults instead of an explicit hands item?
from game.data.items import hands

from . import PrimaryStat, PrimaryStats, SecondaryStats, EquipStat, EquipStats

import game.components as C
from game.items.weapon_type import weapon_physical_stat_assignment, weapon_magical_stat_assignment
from game.items.slots import WeaponSlot
from .stats import Stats

#physical/magical attack are based on weapon attack and the weapon stats

#TODO: also calculate defense stats
#TODO: weapons and armor should have "physical/magical attack/defense" which is multiplicative
#TODO: default physical/magical attack/defense from weapons/armor should be 1

PRIMARY_PATT_MULTIPLIER = 20
SECONDARY_PATT_MULTIPLIER = 10
PRIMARY_MATT_MULTIPLIER = 20
SECONDARY_MATT_MULTIPLIER = 10
VIT_PDEF_MULTIPLIER = 20
WIS_MDEF_MULTIPLIER = 20
VIT_HP_MULTIPLIER = 20
WIS_MP_MULTIPLIER = 20
DEX_ACC_MULTIPLIER = 20
AGI_EVA_MULTIPLIER = 20
AGI_MOVE_MULTIPLIER = 1

BASE_EQUIP_STATS = EquipStats(1, 1, 1, 1)
BASE_PRIMARY_STATS = PrimaryStats(10, 10, 10, 10, 10, 10)
BASE_SECONDARY_STATS = SecondaryStats(
  hp=100,
  mp=50,
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

  base_equip_stats = get_stats_from_equips(entity)
  equip_stats = (base_equip_stats + flat.equip) * scaling.equip

  base_primary_stats = calculate_primary_stats(entity)
  primary_stats = (base_primary_stats + flat.primary) * scaling.primary
  
  base_secondary_stats = calculate_secondary_stats(entity, primary_stats, equip_stats)
  secondary_stats = (base_secondary_stats + flat.secondary) * scaling.secondary
  
  return Stats(
    primary=primary_stats,
    equip=equip_stats,
    secondary=secondary_stats,
  )

def calculate_primary_stats(entity):
  equips = entity.get_component(C.Equips)

  #sum up primary stats
  stats = BASE_PRIMARY_STATS

  for equip in equips.armor.values():
    if equip is not None:
      stats = stats + equip.primary_stats

  for equip in equips.weapons.values():
    if equip is not None:
      stats = stats + equip.primary_stats

  return stats

#TODO: eventually this should return a full Stats
def get_stats_from_equips(entity):
  equips = entity.get_component(C.Equips)

  #sum up equip stats
  stats = BASE_EQUIP_STATS
  
  for equip in equips.armor.values():
    if equip is not None:
      stats = stats + equip.equip_stats

  for equip in equips.weapons.values():
    if equip is not None:
      stats = stats + equip.equip_stats

  return stats

def calculate_secondary_stats(entity, primary_stats, equip_stats):
  #TODO: handle 2h and secondary weapons
  weapon = entity.get_component(C.Equips).weapons[WeaponSlot.PRIMARY]
  if weapon is None:
    weapon = hands

  #TODO: add secondary stats on equips
  #TODO: apply modifiers from passives/buffs/debuffs/etc
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
  )

def calculate_hp(primary_stats):
  return primary_stats.VIT * VIT_HP_MULTIPLIER

def calculate_mp(primary_stats):
  return primary_stats.WIS * WIS_MP_MULTIPLIER

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
