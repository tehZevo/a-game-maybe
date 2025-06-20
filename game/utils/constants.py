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
PLAYER_INVULN_TIME = 1 #seconds
PLAYER_MOVE_SPEED = 1
ENEMY_MOVE_SPEED = 1/4.
CHUNK_SIZE = 16
CAMERA_BOX_SIZE = 1
DOT_TICK_RATE = 0.5 #seconds
NETWORK_POS_MAX_DIST = 1
NETWORK_VEL_MAX_DIST = 0.0
#TODO: this doesnt feel like 1/4..
PHYS_REPORT_RATE = 10 #how often clients report position/velocity (seconds)
REPORT_POS_ERROR_THRESH = 1 #how off client ent pos must be in reports before server corrects

#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300
