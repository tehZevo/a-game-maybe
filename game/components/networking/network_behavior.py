#useful for any component that needs separate server/client behavior
class NetworkBehavior:
  def __init__(self):
    pass

  def start_server(self, networking):
    pass

  def start_client(self, networking):
    pass

  def update_server(self, networking):
    pass

  def update_client(self, networking):
    pass

  def on_destroy_server(self, networking):
    pass

  def on_destroy_client(self, networking):
    pass
