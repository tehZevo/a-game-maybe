import time
import uuid
from queue import Queue, Empty
from threading import Thread

from .server import Server

class LocalConnection:
  def __init__(self, our_messages, their_messages):
    self.messages = our_messages
    self.their_messages = their_messages
  
  def send(self, message):
    self.their_messages.put(message)
  
  def receive_all(self):
    items = []
    while True:
      try: items.append(self.messages.get_nowait())
      except Empty: break
    return items

def make_connection_pair():
  our_messages = Queue()
  their_messages = Queue()
  connection_to_client = LocalConnection(our_messages, their_messages)
  connection_to_server = LocalConnection(their_messages, our_messages)

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

  def start(self):
    def coro():
      while True:
        processed_a_message = False
        for client_id, conn in self.clients.items():
          #TODO: add .disconnect to connection and detect it here? (e.g. client thread blows up)
          for message in conn.receive_all():
            self.on_message(client_id, message)
            processed_a_message = True
        
        # #TODO: async rather than wait
        # if not processed_a_message:
        #   print("[Server] No messages received, sleeping...")
        #   time.sleep(1)
        time.sleep(0)
        
    t = Thread(target=coro, daemon=True)
    t.start()

  def send(self, id, event):
    self.clients[id].send(self.build_event(event))
