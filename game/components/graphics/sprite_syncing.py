from game.ecs import Component
import game.components as C

from game.components.networking.networking import Networking
from game.components.graphics.sprite_listener import SpriteListener

class SpriteSyncing(Component, Networking, SpriteListener):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Sprite, C.Networked)

  def on_sprite_changed(self, sprite):
    #TODO: networked seems like a weird name...
    networked = self.get_component(C.Networked)
    if networked.is_server:
      #TODO: circular import
      from game.networking.events import SpriteChanged
      networked.server_manager.server.broadcast(SpriteChanged(networked.id, sprite.path))
