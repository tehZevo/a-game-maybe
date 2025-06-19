from queue import Empty

class Connection:
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