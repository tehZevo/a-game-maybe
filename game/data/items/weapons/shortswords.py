from game.items.defs import Shortsword
from game.items import EquipGrade as G
from game.items import Rarity as R
from game.stats import Stats

wooden_shortsword = Shortsword(
    id="wooden_shortsword",
    grade=G.E,
    icon="assets/items/weapons/shortswords/wooden_shortsword.png",
    stats=Stats.Equip(PATT=10, MATT=1)
)

copper_shortsword = Shortsword(
    id="copper_shortsword",
    grade=G.E,
    icon="assets/items/weapons/shortswords/copper_shortsword.png",
    stats=Stats.Equip(PATT=15, MATT=2)
)

unobtanium_shortsword = Shortsword(
    id="unobtanium_shortsword",
    grade=G.SS,
    rarity=R.LEGENDARY,
    icon="assets/items/weapons/shortswords/unobtanium_shortsword.png",
    stats=Stats.Equip(PATT=100, MATT=100) + Stats.Primary(1, 1, 1, 1, 1, 1) * 100
)
