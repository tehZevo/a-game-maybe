from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator
import game.data.tile_palettes as P
import game.data.world_map as W

maze = MapDef(
    id="maze",
    palette=P.sand_floors + P.stone_walls,
    generator=DFSGenerator(6, 6, 1, next_maps=W["maze"])
)