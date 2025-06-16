from game.items.defs import Longsword
from game.items import EquipGrade
from game.items import Rarity

wooden_longsword = Longsword(
    id="wooden_longsword",
    grade=EquipGrade.D,
    rarity=Rarity.UNCOMMON,
    icon="assets/items/weapons/longsword.png"
)
