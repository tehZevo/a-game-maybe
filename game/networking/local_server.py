import asyncio
import uuid
from queue import Queue

from .server import Server
from .connection import Connection

def make_connection_pair():
  our_messages = Queue()
  their_messages = Queue()
  connection_to_client = Connection(our_messages, their_messages)
  connection_to_server = Connection(their_messages, our_messages)

  return connection_to_client, connection_to_server

class LocalServer(Server):
  def __init__(self):
    super().__init__()
  
  def connect(self):
    id = str(uuid.uuid4())
    our_conn, their_conn = make_connection_pair()
    self.on_connect(id, our_conn)
    return their_conn
  
  def receive_all(self):
    messages = []
    for id, conn in self.clients.items():
      messages += [[id, m] for m in conn.receive_all()]
    return messages

  async def handle_messages(self):
    for client_id, conn in self.clients.items():
      #TODO: add .disconnect to connection and detect it here? (e.g. client thread blows up)
      for message in conn.receive_all():
        self.on_message(client_id, message)
  
  async def start(self):
    return

  def send(self, id, event):
    self.clients[id].send(self.build_event(event))
