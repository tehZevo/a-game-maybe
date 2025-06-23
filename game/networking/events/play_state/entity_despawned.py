from dataclasses import dataclass

from game.networking import PlayStateEventHandler

@dataclass
class EntityDespawned:
  id: str

class EntityDespawnedHandler(PlayStateEventHandler):
  def __init__(self, game_state):
    super().__init__(EntityDespawned, game_state)

  def handle(self, event):
    client_manager = self.game_state.client_manager
    #TODO: this is caused by entities not being on client yet.. need to sync them when client first "sees" them
    # this either means sending actor spawned for all ents upon player join, OR having other actors/networked components spawn/despawn themselves on the client
    if event.id not in client_manager.networked_entities:
      #print("trying to update entity position with id", event.id, "but not found in networked entities...")
      return
    ent = client_manager.network_unregister(event.id)
    ent.remove()
    # print("[Client] entity despawned:", event.id)
