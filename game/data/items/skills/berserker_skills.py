from game.items import SkillItem, Rarity
import game.data.skills as S

sanguine_strike = SkillItem(
  id="sanguine_strike",
  skilldef=S.sanguine_strike,
  rarity=Rarity.RARE
)

sacrifice = SkillItem(
  id="sacrifice",
  skilldef=S.sacrifice,
  rarity=Rarity.RARE
)
