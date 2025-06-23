from game.ecs import Component
from game.components.networking.network_behavior import NetworkBehavior
from game.components.graphics.icon_listener import IconListener
import game.components as C
import game.networking.events as E

class IconSyncing(Component, NetworkBehavior, IconListener):
  def __init__(self, path=None):
    super().__init__()
    self.require(C.Icon, C.Networking)

  def on_client_join(self, networking, client_id):
    icon = self.get_component(C.Icon)
    networking = self.get_component(C.Networking)
    networking.send_to_client(client_id, E.IconChanged(networking.id, icon.image_path))
  
  def start_server(self, networking):
    icon = self.get_component(C.Icon)
    if icon is None:
      return

    networking.broadcast_synced(E.IconChanged(networking.id, icon.image_path))
    
  def on_icon_changed(self, icon):
    networking = self.get_component(C.Networking)
    if networking.is_server:
      networking.broadcast_synced(E.IconChanged(networking.id, icon.path))
