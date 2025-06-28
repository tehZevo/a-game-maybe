from enum import IntEnum
from game.stats import PrimaryStat as S
from game.items.handedness import Handedness as H
from game.items.slots import WeaponSlot

WeaponType = IntEnum("WeaponType", [
    "SHORTSWORD", "SHORTSWORD_L", "LONGSWORD", "POLEARM", "MACE", "KNUCKLES",
    "BOW", "DAGGER", "DAGGER_L", "REPEATER", "REPEATER_L", 
    "STAFF",
    "SHIELD", "ORB", "TOME"
])
W = WeaponType

swingable_primaries = [W.SHORTSWORD, W.LONGSWORD, W.POLEARM, W.MACE, W.DAGGER, W.STAFF]
can_cast_magic_primaries = swingable_primaries + [W.KNUCKLES]

def weapon_physical_stat_assignment(weapon_type):
    match weapon_type:
        case W.POLEARM | W.MACE: return (S.STR, S.VIT)
        case W.BOW | W.DAGGER | W.DAGGER_L: return (S.DEX, S.STR)
        case W.REPEATER | W.REPEATER_L: return (S.DEX, S.AGI)
    return (S.STR, S.DEX)

def weapon_magical_stat_assignment(weapon_type):
    return (S.INT, S.WIS)

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

def weapon_slot(weapon):
    handedness = weapon_handedness(weapon)
    match handedness:
        case H.ONE_HANDED: return WeaponSlot.PRIMARY
        case H.TWO_HANDED: return WeaponSlot.PRIMARY
        case H.SECONDARY: return WeaponSlot.SECONDARY