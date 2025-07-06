from game.save_data import SaveData
import game.networking.commands as C
import game.networking.events as E
import game.data.maps as M
from game.data.registry import get_map
from game.states import ServerLobbyState, ServerPlayState

#TODO: find a better place for this file?

class ServerRoom:
  def __init__(self, server, channel, join_code, initial_mapdef_id=None):
    self.save_data = SaveData()
    self.server = server
    self.channel = channel
    self.join_code = join_code
    #TODO: dont like all the duplicate storing of player sets (channel, room, state...)
    self.players = set()

    self.initial_mapdef = M.maze if initial_mapdef_id is None else get_map(initial_mapdef_id)

    lobby_channel = server.create_channel()
    self.state = ServerLobbyState(self, lobby_channel)

  @property
  def empty(self):
    return len(self.players) == 0
   
  def on_join(self, client_id):
    self.players.add(client_id)
    self.channel.clients.add(client_id)
    self.state.channel.clients.add(client_id)
  
  def on_disconnect(self, client_id):
    print("[Server] Handling disconnect of client", client_id)
    self.players.remove(client_id)
    if self.state is not None:
      self.state.on_disconnect(client_id)
  
  def get_lobby_channel(self):
    if isinstance(self.state, ServerLobbyState):
      return self.state.channel

    #TODO: consider how to handle
    raise ValueError("Room is not in lobby state")
  
  def begin_game(self):
    channel = self.server.create_channel()
    self.state = ServerPlayState(self, self.initial_mapdef, channel)
    self.state.channel.clients = self.channel.clients #TODO: need better ergo here
    self.channel.broadcast(E.WorldOpened(channel.id))

  def transition(self, mapdef):
    self.channel.broadcast(E.WorldClosed())
    self.server.remove_channel(self.state.channel.id)
    channel = self.server.create_channel()
    channel.clients = self.channel.clients
    self.state = ServerPlayState(self, mapdef, channel)
    self.channel.broadcast(E.WorldOpened(channel.id))

  def step(self):
    self.state.step()
