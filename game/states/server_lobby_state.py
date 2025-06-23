import game.networking.commands as C

class ServerLobbyState:
  def __init__(self, room, channel):
    self.room = room
    self.channel = channel
    self.players_ready = set()

    self.channel.setup_handlers([
      C.PlayerReadyHandler(self)
    ])

  def set_player_ready(self, client_id, ready):
    if ready:
      self.players_ready.add(client_id)
    else:
      self.players_ready.remove(client_id)
    
    #TODO: countdown?
    print(f"[Server] {len(self.players_ready)}/{len(self.room.players)} players ready")

    if len(self.players_ready) > 0 and self.players_ready == set(self.room.players):
      print("[Server] All players ready, beginning game...")
      self.room.begin_game()

  def on_disconnect(self, client_id):
    self.server_manager.player_unregister(client_id)
    self.players_read = set()
  
  def step(self):
    self.channel.handle_commands()
