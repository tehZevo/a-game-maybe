from .command_handler import CommandHandler

class LobbyStateCommandHandler(CommandHandler):
  def __init__(self, command_type, game_state):
    super().__init__(command_type)
    self.game_state = game_state