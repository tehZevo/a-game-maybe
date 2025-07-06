from enum import IntEnum

EquipGrade = IntEnum("EquipGrade", ["UNKNOWN", "E", "D", "C", "B", "A", "S", "SS"])
G = EquipGrade

def equip_grade_icon(rank):
    match rank:
        case G.UNKNOWN: return None
        case G.E: return "assets/icons/e.png"
        case G.D: return "assets/icons/d.png"
        case G.C: return "assets/icons/c.png"
        case G.B: return "assets/icons/b.png"
        case G.A: return "assets/icons/a.png"
        case G.S: return "assets/icons/s.png"
        case G.SS: return "assets/icons/ss.png"