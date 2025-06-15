from dataclasses import dataclass

from ..event_handler import EventHandler
import game.components as C

@dataclass
class IconChanged:
  id: str
  image_path: str | None

class IconChangedHandler(EventHandler):
  def __init__(self):
    super().__init__(IconChanged)

  def handle(self, client_manager, client, event):
    #TODO: fix this
    if event.id not in client_manager.networked_entities:
      print("trying to update entity icon with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.networked_entities[event.id]
    icon = ent.get_component(C.Icon)
    icon.set_image(event.image_path)
