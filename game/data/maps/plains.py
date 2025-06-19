from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator
import game.data.tile_palettes as P
import game.data.world_map as W

plains = MapDef(
    id="plains",
    palette=P.grass_walls + P.grass_floors,
    generator=DFSGenerator(20, 2, 1, next_maps=W["plains"])
)