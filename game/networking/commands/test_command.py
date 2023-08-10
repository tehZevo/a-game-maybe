from dataclasses import dataclass

from ..command_handler import CommandHandler

@dataclass
class TestCommand:
  message: str

class TestCommandHandler(CommandHandler):
  def __init__(self):
    super().__init__(TestCommand)

  def handle(self, server, id, command):
    print("received", command)
