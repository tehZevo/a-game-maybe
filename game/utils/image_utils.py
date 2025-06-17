import pygame

#TODO: test these
def get_frame(surface, frame_width, frame):
  _, height = surface.get_size()
  rect = (frame * frame_width, 0, (frame + 1) * frame_width, height)
  return surface.subsurface(rect)

def get_frame_t(surface, frame_width, t):
  width, height = surface.get_size()
  num_frames = int(width / frame_width)
  frame = int(t * num_frames) % num_frames
  return get_frame(surface, frame_width, frame)

def tint(surface, tint):
  surface = surface.copy()
  surface.fill(tint, special_flags=pygame.BLEND_MULT)
  return surface

def fade(surface, opacity):
  surface = surface.copy()
  surface.set_alpha(alpha)
  return surface