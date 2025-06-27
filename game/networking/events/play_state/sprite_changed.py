from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C
from game.data.registry import get_sprite
from game.utils import Vector

@dataclass
class SpriteChanged:
  entity_id: str
  sprite_id: str | None
  animation: str | None
  time: float
  speed: float
  tint: tuple | None
  alpha: float | None
  offset: Vector | None
  flip_x: bool
  palette: str | None

class SpriteChangedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(SpriteChanged, game_state)

  def handle(self, e):
    manager = self.game_state.client_manager
    ent = manager.networked_entities.get(e.entity_id)
    if ent is None:
      return
    s = ent[C.Sprite]
    s.set_sprite(get_sprite(e.sprite_id))
    s.set_animation(e.animation)
    s.set_speed(e.speed)
    s.set_time(e.time)
    s.tint = e.tint
    s.alpha = e.alpha
    s.offset = e.offset
    s.flip_x = e.flip_x
    s.palette = e.palette
