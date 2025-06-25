#### CORE #####################
#TODO: decouple rendering from physics updates
FPS = 60
DT = 1. / FPS
TILE_SIZE = 16
CHUNK_SIZE = 16
CAMERA_BOX_SIZE = 1

#### ITEMS ####################
# BASE_DROP_RATE = 1/10
BASE_DROP_RATE = 1
ITEM_DROP_RADIUS = 0.5
ITEM_PUSH_DISTANCE = 1.25
ITEM_PUSH_FORCE = 10
MAX_DROPPED_ITEMS = 10

#### ACTOR ####################
DEFAULT_SKILL_USE_TIME = 0.5 #seconds
PLAYER_INVULN_TIME = 1 #seconds
PLAYER_MOVE_SPEED = 1
ENEMY_MOVE_SPEED = 1/4.
DOT_TICK_RATE = 0.5 #seconds

#### PHYSICS ##################
PHYS_REPORT_RATE = 1/4 #how often clients report position/velocity (seconds)
REPORT_POS_ERROR_THRESH = 1 #how off client ent pos must be in reports before server corrects
REPORT_VEL_ERROR_THRESH = 0.1 #how off client ent vel must be in reports before server corrects
#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300

#### OTHER NETWORKING #########
DEV_ROOM_CODE = None