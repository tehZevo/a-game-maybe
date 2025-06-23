from dataclasses import dataclass

from game.networking import PlayStateEventHandler
import game.components as C

@dataclass
class IconChanged:
  id: str
  image_path: str | None

class IconChangedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(IconChanged, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    #TODO: fix this
    if event.id not in client_manager.networked_entities:
      print("trying to update entity icon with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.networked_entities[event.id]
    icon = ent.get_component(C.Icon)
    icon.set_image(event.image_path)
