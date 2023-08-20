import uuid

from game.ecs import Component

class Networked(Component):
  def __init__(self, id=None):
    super().__init__()
    self.id = str(uuid.uuid4()) if id is None else id
    self.is_client = None
    self.is_server = None

  def start(self):
    #TODO: circular reference
    from . import ClientManager, ServerManager
    self.is_client = len(self.entity.world.find_components(ClientManager)) > 0
    self.is_server = not self.is_client

    if self.is_server:
      self.entity.world.find_component(ServerManager).spawn(self.entity)
    else:
      self.entity.world.find_component(ClientManager).spawn(self.entity)

  def on_destroy(self):
    #TODO: circular reference
    from . import ClientManager, ServerManager
    if self.is_server:
      self.entity.world.find_component(ServerManager).despawn(self.entity)
    #call despawn manually on client
    # else:
    #   self.entity.world.find_component(ClientManager).despawn(self.entity)
