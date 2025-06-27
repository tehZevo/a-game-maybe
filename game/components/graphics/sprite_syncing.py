from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from game.components.graphics.sprite_listener import SpriteListener
import game.components as C
import game.networking.events as E

def to_event(id, s):
  return E.SpriteChanged(id, s.sprite and s.sprite.id, s.animation, s.time,
    s.speed, s.tint, s.alpha, s.offset, s.flip_x, s.palette)

class SpriteSyncing(Component, NetworkBehavior, SpriteListener):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Sprite, C.Networking)
  
  def on_client_join(self, networking, client_id):
    sprite = self.get_component(C.Sprite)
    networking = self.get_component(C.Networking)
    evt = to_event(networking.id, sprite)
    networking.send_to_client(client_id, evt)
    
  def on_sprite_changed(self, sprite):
    networking = self.get_component(C.Networking)
    if networking.is_server:
      evt = to_event(networking.id, sprite)
      networking.broadcast_synced(evt)
  
  def start_server(self, networking):
    sprite = self.entity[C.Sprite]
    networking.broadcast_synced(to_event(networking.id, sprite))
