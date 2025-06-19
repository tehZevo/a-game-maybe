import asyncio
import platform

from .client import Client

#TODO: make this not global maybe
QUEUE = asyncio.Queue()
CONNECT_EVENT = asyncio.Event()
#TODO: async lock for awaiting connect

def handle_open():
  CONNECT_EVENT.set()

def handle_message(message):
  asyncio.create_task(QUEUE.put(message))

def handle_close():
  print("TODO: closed")

class JSWSClient(Client):
  def __init__(self, url):
    super().__init__()
    self.url = url
    #TODO: use url when connecting

  async def connect(self):
    with open("main.js", "r") as f:
      platform.window.pythonClientOnOpen = handle_open
      platform.window.pythonClientOnMessage = handle_message
      platform.window.pythonClientOnClose = handle_close
      platform.window.eval(f.read())
    
    await CONNECT_EVENT.wait()
    self.on_connect()
    
    while True:
      message = await QUEUE.get()
      self.on_message(message) #TODO: what format?
    self.on_disconnect()

  def send(self, command):
    command = self.build_command(command)
    platform.window.pythonClientSend(command+"\n")

  def disconnect(self):
    return
    self.writer.close()