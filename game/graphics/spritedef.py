import itertools
import bisect

from pygame import Vector2, Rect

from game.utils.image_cache import get_image
from game.utils.constants import TILE_SIZE
from game.utils import Vector

#TODO: ability to attach objects at points in sprites? (weapons)?
#TODO: ability to composite sprites (sprite_a + sprite_b) for adding armor/equips to player?
#TODO: are spritedefs needed? i think we can collapse id and origin into Animation
class Spritedef:
  def __init__(self, id, animations={}, origin=[0, 0]):
    self.id = id
    self.animations = animations
    self.origin = Vector(*origin)
  
  def draw(self, renderer, tint, alpha, animation, time, position):
    self.animations[animation].draw(renderer, tint, alpha, time, position + self.origin / TILE_SIZE)

class SimpleSprite(Spritedef):
  def __init__(self, id, image_path, frame_width, num_frames, offset=None, loop=False):
    offsets = offset and [offset for _ in range(num_frames)]
    l = Layer(image_path, frame_width, num_frames, offsets=offsets)
    a = Animation(layers=[l], loop=loop)
    super().__init__(id, animations={"default": a})

class Animation:
  def __init__(self, layers=[], frame_times=None, loop=False):
    self.layers = layers
    self.loop = loop
    self.num_frames = self.calc_num_frames(self.layers)
    self.frame_times = self.calc_frame_times(frame_times)
    
  def calc_num_frames(self, layers):
    layer_frames = [l.num_frames for l in layers]
    if not all([f == layer_frames[0] for f in layer_frames]):
      s = ", ".join(layer_frames)
      raise ValueError(f"Layers do not all have the same number of frames: {s}")
    return layer_frames[0]

  def calc_frame_times(self, frame_times):
    if frame_times is None:
      frame_times = [1 / self.num_frames for _ in range(self.num_frames)]
    
    if len(frame_times) != self.num_frames:
      raise ValueError(f"Length of frame times ({len(frame_times)} does match number of frames in layers ({self.num_frames}))")
    
    #rescale and make cumulative
    s = sum(frame_times)
    frame_times = [t / s for t in frame_times]
    return list(itertools.accumulate(frame_times))
  
  def calc_frame(self, t):
    if not self.loop and t < 0: return 0
    if not self.loop and t >= 1: return self.num_frames - 1
    if self.loop:
      t = t % 1
    #TODO: better way to clamp?
    return max(0, min(bisect.bisect_left(self.frame_times, t), self.num_frames - 1))

  def draw(self, renderer, tint, alpha, time, position):
    frame = self.calc_frame(time)
    for layer in self.layers:
      layer.draw(renderer, tint, alpha, frame, position)

class Layer:
  def __init__(self, image_path, frame_width, num_frames, offsets=None):
    self.image_path = image_path
    self.image = None
    self.frame_width = frame_width
    self.num_frames = num_frames
    self.offsets = offsets
    
  def load_image(self):
    self.image = get_image(self.image_path)
    w, h = self.image.get_size()
    self.frame_height = h
    if w % self.frame_width != 0:
      raise ValueError(f"Image '{self.image_path}' width ({w}) is not evenly divisible by frame width ({self.frame_width}).")
    self.num_frames = w // self.frame_width
    
    self.offsets = self.offsets or [[0, 0] for _ in range(self.num_frames)]
    self.offsets = [Vector(x, y) for x, y in self.offsets]
  
  def draw(self, renderer, tint, alpha, frame, position):
    if self.image is None:
      #TODO: i dont like this but images were trying to be loaded at least once on the server..
      #TODO: remove if i can fix that
      self.load_image()
    if self.image is None:
      return
    
    #TODO: for now, we treat offset as pixels and then rescale to world space.. is there a better way?
    offset = self.offsets[frame] / TILE_SIZE
    pos = position + offset
    area = [frame * self.frame_width, 0, self.frame_width, self.frame_height]
    renderer.draw(self.image, position + offset, area=area, tint=tint, alpha=alpha)
