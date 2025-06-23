import game.components as C
import game.networking.events as E
import game.networking.commands as C

class ClientLobbyState:
  def __init__(self, channel):
    self.channel = channel
    self.channel.setup_handlers([
      #TODO
    ])
    
    print("[Client] Hello lobby state")

    #TODO: send hello lobby and await lobbystateupdated
    self.channel.send(C.PlayerReady())
    
  def step(self, pressed, held, released):
    self.channel.handle_events()
