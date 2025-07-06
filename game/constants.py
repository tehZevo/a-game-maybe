#### CORE #####################
FPS = 60
DT = 1. / FPS
TILE_SIZE = 16
CHUNK_SIZE = 16
CAMERA_BOX_SIZE = 1
CONFIG_PATH = "settings.json"
SCREEN_WIDTH_TILES = 16
SCREEN_HEIGHT_TILES = 12
FPS_MEASURE_RATE = 10 #seconds

#### ITEMS ####################
BASE_DROP_RATE = 1/100
ITEM_DROP_RADIUS = 0.5
ITEM_PUSH_DISTANCE = 1.25
ITEM_PUSH_FORCE = 10
MAX_DROPPED_ITEMS = 10

#### GRAPHICS #################
DAMAGE_NUMBER_SEPARATION = 6 / 16 #TODO: use (currently unused in damage number animation)
DAMAGE_NUMBER_STACK_SEPARATION = 12 / 16 #TODO: hardcoded tile size division
DAMAGE_NUMBER_TIME = 1
DAMAGE_NUMBER_STACK_DELAY = 0.25
DAMAGE_NUMBER_HEIGHT = 1

#### ACTOR ####################
DEFAULT_SKILL_USE_TIME = 0.5 #seconds
PLAYER_MOVE_SPEED = 1
ENEMY_MOVE_SPEED = 1/4.
ENEMY_MOVE_UPDATE_TIME = 1
ENEMY_MOVE_DIST_THRESH = 0.5
ENEMY_TARGET_DISTANCE = 5

#### STATS ####################
HP_RECOVERY_PERCENT = 1
MP_RECOVERY_PERCENT = 1
HP_RECOVERY_TIME = 1
MP_RECOVERY_TIME = 1

#### COMBAT ###################
PLAYER_INVULN_TIME = 1 #seconds
DOT_TICK_RATE = 0.5 #seconds
IN_COMBAT_TIME = 5
DAMAGE_SPREAD = 0.5

#### INTERACT #################
INTERACT_RADIUS = 1
INTERACT_TARGET_UPDATE_TIME = 0.25
INTERACT_TARGET_DISTANCE = 0.5

#### PHYSICS ##################
PHYS_REPORT_RATE = 1/4 #how often clients report position/velocity (seconds)
REPORT_POS_ERROR_THRESH = 1 #how off client ent pos must be in reports before server corrects
REPORT_VEL_ERROR_THRESH = 0.1 #how off client ent vel must be in reports before server corrects
#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300

#### OTHER NETWORKING #########
DEV_ROOM_CODE = None