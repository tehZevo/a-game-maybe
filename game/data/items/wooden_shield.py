from game.items.defs import Shield
from game.items import EquipGrade
from game.items import Rarity

wooden_shield = Shield(
    id="wooden_shield",
    grade=EquipGrade.C,
    rarity=Rarity.RARE,
    icon="assets/items/weapons/shield.png"
)
