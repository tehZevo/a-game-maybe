from game.items import SkillItem, Rarity
import game.data.skills as S

bless = SkillItem(
  id="bless",
  skilldef=S.bless,
  rarity=Rarity.RARE
)

magic_bolt = SkillItem(
  id="magic_bolt",
  skilldef=S.magic_bolt,
  rarity=Rarity.COMMON
)

fireball = SkillItem(
  id="fireball",
  skilldef=S.fireball,
  rarity=Rarity.COMMON
)

heal = SkillItem(
  id="heal",
  skilldef=S.heal,
  rarity=Rarity.COMMON
)
