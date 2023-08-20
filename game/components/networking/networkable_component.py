from game.ecs import Component
from . import Id

class NetworkableComponent(Component):
  def __init__(self):
    super().__init__()
    self.require(Id)
    self.is_client = None
    self.is_server = None
    self.server_manager = None
    self.client_manager = None
    #TODO: aliases like server, client server.broadcast, server.send, etc

  def start(self):
    #TODO: circular reference
    from . import ClientManager, ServerManager, Id
    self.is_client = len(self.entity.world.find_components(ClientManager)) > 0
    self.is_server = not self.is_client

    if self.is_server:
      self.server_manager = self.entity.world.find_component(ServerManager)
      self.server_manager.spawn(self.entity)
      self.start_server()
    else:
      self.client_manager = self.entity.world.find_component(ClientManager)
      self.client_manager.spawn(self.entity)
      self.start_client()

  def update(self):
    if self.is_server:
      self.update_server()
    else:
      self.update_client()

  def start_server(self):
    pass

  def start_client(self):
    pass

  def update_server(self):
    pass

  def update_client(self):
    pass

  def on_destroy(self):
    if self.is_server:
      self.server_manager.despawn(self.entity)
      self.on_destroy_server()
    else:
      self.on_destroy_client()

  def on_destroy_server(self):
    pass

  def on_destroy_client(self):
    pass
