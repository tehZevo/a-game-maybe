
class CommandHandler:
  def __init__(self, command_type):
    self.command_type = command_type

  #TODO: remove either server_manager or server
  def handle(self, server_manager, server, client_id, command):
    raise NotImplementedError
