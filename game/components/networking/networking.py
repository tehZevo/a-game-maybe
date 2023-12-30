import uuid

from game.ecs import Component
from game.networking.events import EntitySpawned, EntityDespawned
import game.components as C

class Networking(Component):
  def __init__(self, id=None):
    super().__init__()
    self.id = id
    self.is_client = None
    self.is_server = None
    self.server_manager = None
    self.client_manager = None

  def start(self):
    #NOTE: technically possible to be neither client or server.. eg ui world
    self.is_client = len(self.entity.world.find_components(C.ClientManager)) > 0
    self.is_server = len(self.entity.world.find_components(C.ServerManager)) > 0

    if self.is_server:
      self.start_server()
    elif self.is_client:
      self.start_client()

  def update(self):
    if self.is_server:
      self.update_server()
    elif self.is_client:
      self.update_client()

  def for_all_networking(self, fn):
    for component in self.entity.components.values():
      if not isinstance(component, C.NetworkBehavior):
        continue
      fn(component)

  def on_destroy(self):
    if self.is_server:
      #auto despawn
      self.server_manager.network_unregister(self.entity)
      self.server_manager.server.broadcast(EntityDespawned(self.id))
      self.on_destroy_server()
    elif self.is_client:
      self.on_destroy_client()

  def start_server(self):
    #set up id and server manager
    self.id = str(uuid.uuid4()) if self.id is None else self.id
    self.server_manager = self.entity.world.find_component(C.ServerManager)
    self.server_manager.network_register(self.entity)

    #spawn entity on start
    self.server_manager.server.broadcast(EntitySpawned(self.id, self.get_spawn_components()))

    #call start_client on all networking components
    self.for_all_networking(lambda c: c.start_server(self))

  def start_client(self):
    #set up client manager
    self.client_manager = self.entity.world.find_component(C.ClientManager)
    self.client_manager.network_register(self.entity)

    #call start_client on all networking components
    self.for_all_networking(lambda c: c.start_client(self))

  def update_server(self):
    #call update_server on all networking components
    self.for_all_networking(lambda c: c.update_server(self))

  def update_client(self):
    #call update_client on all networking components
    self.for_all_networking(lambda c: c.update_client(self))

  def on_destroy_server(self):
    #call on_destroy_server on all networking components
    self.for_all_networking(lambda c: c.on_destroy_server(self))

  def on_destroy_client(self):
    #call on_destroy_client on all networking components
    self.for_all_networking(lambda c: c.on_destroy_client(self))

  def get_spawn_components(self):
    #spawn entity with all networking components
    #- networking components responsible for declaring requirements
    spawn_components = [e.__class__.__name__ for e in self.entity.components.values() if isinstance(e, C.NetworkBehavior)]
    return spawn_components
