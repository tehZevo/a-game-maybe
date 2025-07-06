from enum import IntEnum
from game.stats import PrimaryStat as PS
from game.stats import PrimaryStats
from game.stats import EquipStats
from game.items.handedness import Handedness as H
from game.items.slots import WeaponSlot

WeaponType = IntEnum("WeaponType", [
    "SHORTSWORD", "SHORTSWORD_L", "LONGSWORD", "POLEARM", "MACE", "KNUCKLES",
    "BOW", "DAGGER", "DAGGER_L", "REPEATER", "REPEATER_L", 
    "STAFF",
    "SHIELD", "ORB", "TOME"
])
W = WeaponType

WeaponSpeed = IntEnum("WeaponSpeed", "VERY_SLOW", "SLOW", "MEDIUM", "FAST", "VERY FAST")
WS = WeaponSpeed

swingable_primaries = [W.SHORTSWORD, W.LONGSWORD, W.POLEARM, W.MACE, W.DAGGER, W.STAFF]
can_cast_magic_primaries = swingable_primaries + [W.KNUCKLES]

#TODO: move these kinds of things to calculator folder?
def weapon_physical_stat_assignment(weapon_type):
    match weapon_type:
        case W.POLEARM | W.MACE: return (PS.STR, PS.VIT)
        case W.BOW | W.DAGGER | W.DAGGER_L: return (PS.DEX, PS.STR)
        case W.REPEATER | W.REPEATER_L: return (PS.DEX, PS.AGI)
    return (PS.STR, PS.DEX)

def weapon_magical_stat_assignment(weapon_type):
    return (PS.INT, PS.WIS)

def weapon_handedness(weapon_type):
    match weapon_type:
        case W.LONGSWORD | W.POLEARM | W.BOW | W.KNUCKLES: return H.TWO_HANDED
        case W.SHORTSWORD_L | W.DAGGER_L | W.REPEATER_L | W.SHIELD | W.ORB | W.TOME: return H.SECONDARY
    return H.ONE_HANDED

def valid_weapon_pair(primary, secondary):
    if primary == None or secondary == None:
        return True
    match primary:
        case W.SHORTSWORD | W.MACE | W.DAGGER:
            return secondary in {W.SHORTSWORD_L, W.DAGGER_L, W.SHIELD}
        case W.REPEATER:
            return secondary in {W.REPEATER_L}
        case W.STAFF:
            return secondary in {W.SHIELD, W.ORB, W.TOME}
    return False

def weapon_slot(weapon_type):
    handedness = weapon_handedness(weapon_type)
    match handedness:
        case H.ONE_HANDED: return WeaponSlot.PRIMARY
        case H.TWO_HANDED: return WeaponSlot.PRIMARY
        case H.SECONDARY: return WeaponSlot.SECONDARY

def weapon_speed(weapon_type):
    match weapon_type:
        case W.DAGGER: return WS.VERY_FAST
        case W.SHORTSWORD | W.KNUCKLES | W.REPEATER: return WS.FAST
        case W.MACE | W.BOW: return WS.MEDIUM
        case W.LONGSWORD | W.BOW | W.STAFF: return WS.SLOW
        case W.POLEARM: return WS.VERY_SLOW
    return WS.MEDIUM

def weapon_speed_modifier(weapon_speed):
    match weapon_speed:
        case WS.VERY_FAST: return 0.8
        case WS.FAST: return 0.9
        case WS.MEDIUM: return 1.0
        case WS.SLOW: return 1.1
        case WS.VERY_SLOW: return 1.2

def default_weapon_primary_archetype(weapon_type):
    match weapon_type:
        case W.SHORTSWORD | W.SHORTSWORD_L | W.LONGSWORD | W.KNUCKLES:
            return PrimaryStats(2, 0, 1, 0, 0, 0)
        case W.POLEARM:
            return PrimaryStats(2, 1, 0, 0, 0, 0)
        case W.MACE:
            return PrimaryStats(2, 1, 0, 0, 0, 0)
        case W.DAGGER | W.DAGGER_L:
            return PrimaryStats(1, 0, 2, 0, 0, 0)
        case W.BOW:
            return PrimaryStats(1, 0, 2, 0, 0, 0)
        case W.REPEATER | W.REPEATER_L:
            return PrimaryStats(0, 0, 2, 1, 0, 0)
        case W.STAFF:
            return PrimaryStats(0, 0, 0, 0, 2, 0)
        case W.ORB:
            return PrimaryStats(0, 0, 0, 0, 0, 1)
        case W.TOME:
            return PrimaryStats(0, 0, 0, 0, 1, 0)
    return PrimaryStats()

def default_weapon_equip_archetype(weapon_type):
    #TODO make slower weapons like 1.1 or 1.2?
    match weapon_type:
        case W.SHORTSWORD | W.SHORTSWORD_L | W.LONGSWORD | W.POLEARM | W.MACE \
            | W.DAGGER | W.DAGGER_L | W.BOW | W.REPEATER | W.REPEATER_L:
            return EquipStats(1, 0, 0, 0)
        case W.STAFF:
            return EquipStats(0, 0, 1, 0)
    return EquipStats(0, 0, 0, 0)
