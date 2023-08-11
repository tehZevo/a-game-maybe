from dataclasses import dataclass

from ..event_handler import EventHandler
from game.components.actor import Actor
from game.components.networking import Id
from game.components.graphics import Sprite

import pprint

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
    #create an actor with an id so we can control it like a puppet from the server side
    entity = self.client_manager.entity.world.create_entity([
      Id(event.id),
      #TODO: dont give the entity a hat sprite by default
      Sprite(),
      Actor(),
    ])
    entity.get_component(Sprite).set_sprite("assets/items/armor/hat.png")
    print("actor created:", entity)
