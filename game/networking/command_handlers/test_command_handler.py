from .command_handler import CommandHandler
from ..commands.test_command import TestCommand

class TestCommandHandler(CommandHandler):
  def __init__(self):
    super().__init__(TestCommand)

  def handle(self, server, id, command):
    print("received", command)
