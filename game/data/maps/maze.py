from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator

maze = MapDef(
    generator=DFSGenerator()
)