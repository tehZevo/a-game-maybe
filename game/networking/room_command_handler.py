from .command_handler import CommandHandler

class RoomCommandHandler(CommandHandler):
  def __init__(self, command_type, room):
    super().__init__(command_type)
    self.room = room