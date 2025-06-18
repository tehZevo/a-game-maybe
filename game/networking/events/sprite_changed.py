from dataclasses import dataclass

from ..event_handler import EventHandler
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

class SpriteChangedHandler(EventHandler):
  def __init__(self):
    super().__init__(SpriteChanged)

  def handle(self, client_manager, client, event):
    #TODO: fix this
    if event.entity_id not in client_manager.networked_entities:
      print("trying to update entity sprite with id", event.entity_id, "but not found in networked entities...")
      return
    ent = client_manager.networked_entities[event.entity_id]
    sprite = ent.get_component(C.Sprite)
    sprite.set_sprite(get_sprite(event.sprite_id))
    sprite.set_animation(event.animation)
    sprite.set_speed(event.speed)
    sprite.set_time(event.time)
    sprite.tint = event.tint
    sprite.alpha = event.alpha
    sprite.offset = event.offset
