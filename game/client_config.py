import os
import platform
import json

from game.client_mode import ClientMode
from game.constants import CONFIG_PATH

CONFIG_KEYS = ["server_url"]

class ClientConfig:
  def __init__(self, mode):
    self.server_url = None
    self.mode = mode
  
  def set_server_url(self, url):
    self.server_url = url
    self.save()
    print("[Client] Server url set to:", url)
    
  def to_dict(self):
    return {k: self.__dict__[k] for k in CONFIG_KEYS}
  
  def from_dict(self, d):
    self.__dict__.update({k: d.get(k) for k in CONFIG_KEYS})

  def save(self):
    if self.mode == ClientMode.DESKTOP:
      self.save_to_disk()
    elif self.mode == ClientMode.WEB:
      self.save_to_local_storage()

  def load(self):
    if self.mode == ClientMode.DESKTOP:
      self.load_from_disk()
    elif self.mode == ClientMode.WEB:
      self.load_from_local_storage()

  def load_from_disk(self):
    if os.path.exists(CONFIG_PATH):
      with open(CONFIG_PATH, "r") as f:
        self.from_dict(json.loads(f.read()) or {})

  def load_from_local_storage(self):
    config = platform.window.localStorage.getItem("settings") or "{}"
    config = json.loads(config)
    self.from_dict(config)

  def save_to_disk(self):
    with open(CONFIG_PATH, "w") as f:
      f.write(json.dumps(self.to_dict()))
  
  def save_to_local_storage(self):
    platform.window.localStorage.setItem("settings", json.dumps(self.to_dict()))