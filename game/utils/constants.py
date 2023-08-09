#TODO: decouple rendering from physics updates
FPS = 60
DT = 1. / FPS
BASE_SPRITE_SIZE = 32
PIXEL_SCALE = 1
PPU = BASE_SPRITE_SIZE * PIXEL_SCALE

#scale factor to use since pygame rects are int-only
#allows for fixed point ish collisions
PHYS_SCALE = 300
