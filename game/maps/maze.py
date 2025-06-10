from .mapdef import MapDef
from .generators import DFSGenerator

maze = MapDef(
    generator=DFSGenerator()
)