import uuid

from game.ecs import Component
import game.networking.events as E
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

  def broadcast_all(self, event):
    """Send to all clients regardless of if they've loaded the world (synced)"""
    #shorthand for self.server_manager.server.broadcast(e)
    self.server_manager.server.broadcast(event)
  
  def broadcast_synced(self, event):
    """Send to all synced clients"""
    for client_id in list(self.server_manager.player_entity_map.keys()):
      self.server_manager.server.send(client_id, event)

  def on_destroy(self):
    if self.is_server:
      #auto despawn
      self.server_manager.network_unregister(self.entity)
      self.broadcast_synced(E.EntityDespawned(self.id))
      self.on_destroy_server()
    elif self.is_client:
      self.on_destroy_client()

  #spawn for specific player id
  def spawn(self, client_id):
    self.send_to_client(client_id, E.EntitySpawned(self.id, self.get_spawn_components()))

  def send_to_client(self, client_id, event):
    self.server_manager.server.send(client_id, event)
  
  def send_to_server(self, command):
    self.client_manager.client.send(command)

  #TODO: rename to on_client_sync
  def on_client_join(self, client_id):
    self.for_all_networking(lambda c: c.on_client_join(self, client_id))
  
  def start_server(self):
    #set up id and server manager
    self.id = str(uuid.uuid4()) if self.id is None else self.id
    self.server_manager = self.entity.world.find_component(C.ServerManager)
    self.server_manager.network_register(self.entity)

    #spawn entity on start
    self.broadcast_synced(E.EntitySpawned(self.id, self.get_spawn_components()))

    #call start_server on all networking components
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