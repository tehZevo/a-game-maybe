from game.items.defs import Knuckles
from game.stats import Stats

#a "dummy" weapon for when you have no weapon equipped
hands = Knuckles(
  stats=Stats.Equip(PATT=1, MATT=1)
)
