from game.items.defs import Knuckles
from game.stats import Stats, PrimaryStats

#a "dummy" weapon for when you have no weapon equipped
hands = Knuckles(
  primary_archetype=PrimaryStats(),
  bonus_stats=Stats.Equip(PATT=1, MATT=1)
)
