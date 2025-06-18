import pygame

#TODO: test these
def get_frame(surface, frame_width, frame):
  _, height = surface.get_size()
  rect = (frame * frame_width, 0, frame_width, height)
  return surface.subsurface(rect)

def get_frame_t(surface, frame_width, t, clamp=False):
  width, height = surface.get_size()
  num_frames = int(width / frame_width)
  frame = int(t * num_frames)
  frame = frame % num_frames if not clamp else max(0, min(frame, num_frames - 1))
  return get_frame(surface, frame_width, frame)

def tint(surface, tint):
  surface = surface.copy()
  surface.fill(tint, special_flags=pygame.BLEND_MULT)
  return surface

def fade(surface, opacity):
  surface = surface.copy()
  surface.set_alpha(alpha)
  return surface