from game.tiles import TilePalette as P
from game.tiles import TileType as T

t = lambda x: f"assets/tiles/{x}.png"

grass_floors = P.Floors(t("grass"), t("dirt"))
grass_walls = P.Walls(t("grass"), t("dirt"))
stone_floors = P.Floors(t("stone"), t("sand"))
stone_walls = P.Walls(t("stone"), t("stone"))
sand_floors = P.Floors(t("sand"), t("grass"))
sand_walls = P.Walls(t("sand"), t("grass"))
forest_floors = P.Floors(t("dark_forest"), t("grass"))
forest_walls = P.Walls(t("dark_forest"), t("grass"))
dirt_floors = P.Floors(t("dirt"), t("dark_dirt"))
dirt_walls = P.Walls(t("dirt"), t("dark_dirt"))