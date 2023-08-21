from dataclasses import dataclass

from ..event_handler import EventHandler

#TODO: make this a generic entity_spawned?
#TODO: then how would i choose which components to create on the client side?

@dataclass
class ActorSpawned:
  id: str

class ActorSpawnedHandler(EventHandler):
  def __init__(self, client_manager):
    super().__init__(ActorSpawned)
    self.client_manager = client_manager

  def handle(self, client, event):
    #TODO: circular import
    from game.components.graphics import Sprite
    from game.components.networking import Id
    from game.components.actor import Actor
    #create an actor with an id so we can control it like a puppet from the server side
    entity = self.client_manager.entity.world.create_entity([
      Id(event.id),
      Actor(),
    ])
    #TODO: dont give the entity a hat sprite by default
    entity.get_component(Sprite).set_sprite("assets/items/armor/hat.png")
    print("[Client] Actor spawned:", entity, event.id)
