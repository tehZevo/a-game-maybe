from dataclasses import dataclass

from ..event_handler import EventHandler
import game.components as C

@dataclass
class SpriteChanged:
  id: str
  path: str

class SpriteChangedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(SpriteChanged)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: this is caused by entities not being on client yet.. need to sync them when client first "sees" them
    # this either means sending actor spawned for all ents upon player join, OR having other actors/networked components spawn/despawn themselves on the client
    if event.id not in self.client_manager.networked_entities:
      print("trying to update entity sprite with id", event.id, "but not found in networked entities...")
      return
    ent = self.client_manager.networked_entities[event.id]
    if ent is not None:
      ent.get_component(C.Sprite).set_sprite(event.path)
