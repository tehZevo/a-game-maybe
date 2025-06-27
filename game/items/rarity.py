from enum import IntEnum

Rarity = IntEnum("Rarity", ["COMMON", "RARE", "EPIC", "LEGENDARY"])

def rarity_color(rarity):
    match rarity:
        case Rarity.COMMON: return (230, 230, 230)
        case Rarity.RARE: return (100, 160, 230)
        case Rarity.EPIC: return (160, 0, 255)
        case Rarity.LEGENDARY: return (230, 150, 50)

def rarity_drop_rate(rarity):
    match rarity:
        case Rarity.COMMON: return 1
        case Rarity.RARE: return 1/2
        case Rarity.EPIC: return 1/4
        case Rarity.LEGENDARY: return 1/8
    return 1