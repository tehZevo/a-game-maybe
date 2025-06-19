from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator
import game.data.tile_palettes as P
import game.data.world_map as W

forest = MapDef(
    id="forest",
    palette=P.forest_walls + P.grass_floors,
    generator=DFSGenerator(8, 3, 1, next_maps=W["forest"])
)