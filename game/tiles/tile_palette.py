from game.tiles import TileType as T

#maps tile types to images
class TilePalette:
    def Floors(floors, accent=None): return TilePalette({
        T.FLOOR: floors,
        T.FLOOR_ACCENT: accent
    })
    
    def Walls(walls, accent=None): return TilePalette({
        T.WALL: walls,
        T.WALL_ACCENT: accent
    })

    def __init__(self, palette=None):
        self.palette = palette or {}

    def __add__(self, other):
        return TilePalette({**self.palette, **other.palette})
    
    def __getitem__(self, key):
        return self.palette.get(key)
