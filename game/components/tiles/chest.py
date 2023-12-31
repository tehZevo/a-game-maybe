from game.utils.floor_transition import floor_transition
from ..core import Interactable
from . import TileEntity
import game.components as C
from game.utils import Vector

SPAWN_FORCE = 1000

class Chest(TileEntity, Interactable):
  def __init__(self, items=[]):
    super().__init__()
    self.require(C.Sprite, C.ChestNetworking, C.Networking, C.ItemDropper)
    self.items = items

  def start(self):
    self.get_component(C.Sprite).set_sprite("assets/tiles/chest.png")

  def interact(self, entity):
    dropper = self.get_component(C.ItemDropper)
    pos = self.get_component(C.Position)
    for item in self.items:
      dropped_item = dropper.drop(item, pos.pos)
      spawn_force = Vector.random() * SPAWN_FORCE
      dropped_item.get_component(C.Physics).apply_force(spawn_force)

    self.entity.remove()
