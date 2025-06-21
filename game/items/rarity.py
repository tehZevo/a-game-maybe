from enum import IntEnum

Rarity = IntEnum("Rarity", ["COMMON", "UNCOMMON", "RARE", "EPIC", "LEGENDARY"])

def rarity_color(rarity):
    match rarity:
        case Rarity.COMMON: return (230, 230, 230)
        case Rarity.UNCOMMON: return (100, 230, 100)
        case Rarity.RARE: return (100, 160, 230)
        case Rarity.EPIC: return (160, 0, 255)
        case Rarity.LEGENDARY: return (230, 150, 50)

def rarity_drop_rate(rarity):
    match rarity:
        case Rarity.COMMON: return 1
        case Rarity.UNCOMMON: return 1/2
        case Rarity.RARE: return 1/4
        case Rarity.EPIC: return 1/8
        case Rarity.LEGENDARY: return 1/16
    return 1