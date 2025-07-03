from enum import IntEnum

DamageNumberType = IntEnum("DamageNumberType", ["NORMAL", "HEAL", "CRIT"])
D = DamageNumberType

def damage_number_color(damage_type):
  match damage_type:
    case D.NORMAL: return (255, 247, 206)
    case D.HEAL: return (192, 255, 219)
    case D.CRIT: return (255, 148, 148)