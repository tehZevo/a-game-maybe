from game.items.defs import Shield
from game.items import EquipGrade as G

wooden_shield = Shield(
    id="wooden_shield",
    grade=G.E,
    icon="assets/items/weapons/shields/wooden_shield.png"
)

copper_shield = Shield(
    id="copper_shield",
    grade=G.D,
    icon="assets/items/weapons/shields/copper_shield.png"
)
