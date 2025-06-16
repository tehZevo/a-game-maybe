from enum import IntEnum

SkillRank = IntEnum("SkillRank", ["I", "II", "III", "IV"])

def skill_rank_icon(rank):
    match rank:
        case SkillRank.I: return "assets/icons/i.png"
        case SkillRank.II: return "assets/icons/ii.png"
        case SkillRank.III: return "assets/icons/iii.png"
        case SkillRank.IV: return "assets/icons/iv.png"