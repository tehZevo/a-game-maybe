from game.maps.mapdef import MapDef
from game.maps.generators import DFSGenerator
from game.tiles import TilePalette, TileType

grass_floors = TilePalette({
    TileType.FLOOR: "assets/tiles/tile_grass.png"
})

stone_walls = TilePalette({
    TileType.WALL: "assets/tiles/tile_stone.png"
})

maze = MapDef(
    id="maze",
    palette=grass_floors + stone_walls,
    generator=DFSGenerator()
)