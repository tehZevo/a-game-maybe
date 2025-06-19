import asyncio
import platform

from .client import Client

#TODO: make this not global maybe
QUEUE = asyncio.Queue()
CONNECT_EVENT = asyncio.Event()

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

  async def connect(self):
    #load js client code in browser and set up handlers
    with open("main.js", "r") as f:
      platform.window.eval(f.read())
      platform.window.pythonClientOnOpen = handle_open
      platform.window.pythonClientOnMessage = handle_message
      platform.window.pythonClientOnClose = handle_close
      platform.window.pythonClientConnect(self.url)
    
    await CONNECT_EVENT.wait()
    self.on_connect()
    
    while True:
      message = await QUEUE.get()
      self.on_message(message)
    self.on_disconnect()

  def send(self, command):
    command = self.build_command(command)
    platform.window.pythonClientSend(command+"\n")

  def disconnect(self):
    raise NotImplementedError