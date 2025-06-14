#TODO: decouple rendering from physics updates
FPS = 60
DT = 1. / FPS
TILE_SIZE = 16
# BASE_DROP_RATE = 1/10
BASE_DROP_RATE = 1
DEFAULT_SKILL_USE_TIME = 0.5 #seconds
ITEM_DROP_RADIUS = 0.5
ITEM_PUSH_DISTANCE = 1.25
ITEM_PUSH_FORCE = 10

#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300
