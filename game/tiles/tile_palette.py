
#maps tile types to images
class TilePalette:
    def __init__(self, palette=None):
        self.palette = {} if palette is None else palette

    def __add__(self, other):
        return TilePalette({**self.palette, **other.palette})
    
    def __getitem__(self, key):
        return self.palette.get(key)