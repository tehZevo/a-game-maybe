from dataclasses import dataclass

from ..event_handler import EventHandler

@dataclass
class EntityDespawned:
  id: str

class EntityDespawnedHandler(EventHandler):
  def __init__(self):
    super().__init__(EntityDespawned)

  def handle(self, client_manager, client, event):
    #TODO: this is caused by entities not being on client yet.. need to sync them when client first "sees" them
    # this either means sending actor spawned for all ents upon player join, OR having other actors/networked components spawn/despawn themselves on the client
    if event.id not in client_manager.networked_entities:
      #print("trying to update entity position with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.network_unregister(event.id)
    ent.remove()
    # print("[Client] entity despawned:", event.id)
