import time
import random
from threading import Thread

from .client import Client

class LocalClient(Client):
  def __init__(self, server):
    super().__init__()
    self.server = server
    self.connection = None

  def connect(self):
    self.connection = self.server.connect()
    self.on_connect()
    
    def coro():
      while True:
        processed_a_message = False
        for message in self.connection.receive_all():
          self.on_message(message)
          processed_a_message = True
        
        # #TODO: async rather than wait
        # if not processed_a_message:
        #   print("[Client] No messages received, sleeping...")
        #   time.sleep(1)
        time.sleep(0)

    t = Thread(target=coro, daemon=True)
    t.start()

  def send(self, command):
    self.connection.send(self.build_command(command))

  def disconnect(self):
    raise NotImplementedError