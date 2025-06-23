from .command_handler import CommandHandler

class GameCommandHandler(CommandHandler):
  def __init__(self, command_type, game):
    super().__init__(command_type)
    self.game = game