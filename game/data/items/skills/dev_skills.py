from game.items import SkillItem, Rarity
import game.data.skills as S

dev_die = SkillItem(
  id="dev_die",
  skilldef=S.dev_die,
  rarity=Rarity.LEGENDARY
)

dev_heal = SkillItem(
  id="dev_heal",
  skilldef=S.dev_heal,
  rarity=Rarity.LEGENDARY
)

dev_rush = SkillItem(
  id="dev_rush",
  skilldef=S.dev_rush,
  rarity=Rarity.LEGENDARY,
)

