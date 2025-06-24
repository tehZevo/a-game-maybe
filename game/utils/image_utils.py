import pygame
from game.utils.image_cache import get_image
from game.utils.vector import Vector

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

def text_to_surfaces(text):
  font = get_image("assets/ui/font.png")
  text = text.encode("ascii")
  surfs = []
  for c in text:
    x = (c % 16) * 8
    y = (c // 16) * 8
    surfs.append(font.subsurface((x, y, 8, 8)))
  return surfs

#TODO: for now, w/h are full 8x8 chunks of the 9patch
def draw_9patch(renderer, image_path, offset, w, h):
  image = get_image(image_path)
  def get_patch(x, y):
    px = 0 if x == 0 else 2 if x == w - 1 else 1
    py = 0 if y == 0 else 2 if y == h - 1 else 1
    return image.subsurface((px * 8, py * 8, 8, 8))

  for y in range(h):
    for x in range(w):
      patch = get_patch(x, y)
      renderer.draw(patch, offset + Vector(x * 8, y * 8))

def draw_text(renderer, text, offset, color=(0, 0, 0)):
  surfaces = text_to_surfaces(text)
  for i, surf in enumerate(surfaces):
    renderer.draw(surf, offset + Vector(i * 8, 0), tint=color)