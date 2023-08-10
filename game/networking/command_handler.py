
class CommandHandler:
  def __init__(self, command_type):
    self.command_type = command_type

  def handle(server, id, command):
    raise NotImplementedError
