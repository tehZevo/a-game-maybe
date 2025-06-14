#TODO: decouple rendering from physics updates
FPS = 60
DT = 1. / FPS
TILE_SIZE = 16
# BASE_DROP_RATE = 1/10
BASE_DROP_RATE = 1
DEFAULT_SKILL_USE_TIME = 0.5 #seconds

#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300
