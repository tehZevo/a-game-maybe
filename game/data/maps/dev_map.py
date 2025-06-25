from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator
import game.data.tile_palettes as P
import game.data.world_map as W

dev_map = MapDef(
    id="dev_map",
    palette=P.grass_floors + P.stone_walls,
    generator=DFSGenerator(8, 1, 1, next_maps=["dev_map"])
)