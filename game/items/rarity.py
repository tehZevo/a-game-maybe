from enum import IntEnum

Rarity = IntEnum("Rarity", ["COMMON", "UNCOMMON", "RARE", "EPIC", "LEGENDARY"])

def base_drop_rate(rarity):
    match rarity:
        case Rarity.COMMON: return 1
        case Rarity.UNCOMMON: return 1/2
        case Rarity.RARE: return 1/4
        case Rarity.EPIC: return 1/8
        case Rarity.LEGENDARY: return 1/16
    return 1