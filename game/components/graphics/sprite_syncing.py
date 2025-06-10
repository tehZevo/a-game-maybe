from game.ecs import Component
import game.components as C

from game.components.networking.network_behavior import NetworkBehavior
from game.components.graphics.sprite_listener import SpriteListener

class SpriteSyncing(Component, NetworkBehavior, SpriteListener):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Sprite, C.Networking)

  def on_client_join(self, networking, client_id):
    from game.networking.events import SpriteChanged
    sprite = self.get_component(C.Sprite)
    networking = self.get_component(C.Networking)
    networking.send_to_client(client_id, SpriteChanged(networking.id, sprite.path))
  
  def on_sprite_changed(self, sprite):
    from game.networking.events import SpriteChanged

    networking = self.get_component(C.Networking)
    if networking.is_server:
      networking.broadcast(SpriteChanged(networking.id, sprite.path))
