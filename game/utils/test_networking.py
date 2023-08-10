from .networking import Server, Client

#TODO: update to use events/commands/handlers or remove

class TestServer(Server):
  def __init__(self):
    super().__init__(self.on_connect, self.on_disconnect, self.on_message)

  def on_connect(self, id):
    print("[server]", id, "connected")

  def on_disconnect(self, id):
    print("[server]", id, "disconnected")

  def on_message(self, id, message):
    print(f"[server] ({id}):", message)
    print("[server] sending pong")
    self.send(id, "pong")

class TestClient(Client):
  def __init__(self):
    super().__init__()

  def on_connect(self):
    print("[client] sending ping")
    self.send("ping")

  def on_message(self, message):
    print("[client] received", message)
    self.disconnect()

# TestServer().start()
# TestClient().connect()
