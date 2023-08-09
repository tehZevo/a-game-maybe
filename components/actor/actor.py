from ecs import Component
from components.physics.physics import Physics
from components.physics.collisions import Collisions
from components.graphics.sprite import Sprite
from components.actor.stats import Stats
from components.actor.damage_listener import DamageListener
from components.item.item_dropper import ItemDropper
from components.item.equips import Equips
from utils import Vector

class Actor(Component):
  def __init__(self):
    super().__init__()
    self.require(Physics)
    self.require(Sprite)
    self.require(Stats)
    self.require(ItemDropper)
    self.require(Equips)
    self.require(Collisions)
    self.action = None
    self.next_action = None
    self.look_dir = Vector(0, -1)

  def damage(self, amount):
    stats = self.get_component(Stats)
    stats.hp -= amount
    #find all damage listeners and call their on_damage
    for listener in self.entity.find(DamageListener):
      #TODO: add source
      source = None
      listener.on_damage(source)

  def start_action(self, action):
    self.action = action
    self.action.register(self.entity)
    self.action.start()

  def act(self, action, force=False):
    if force or self.action is None or self.action.interruptible:
      self.start_action(action)
    else:
      self.next_action = action

  def update(self):
    stats = self.get_component(Stats)
    if stats.hp <= 0:
      self.entity.remove()

    if not self.entity.alive:
      return

    #update current action
    if self.action is not None:
      self.action.update()

      #start new action if old action is finished
      if not self.action.active and self.next_action is not None:
        self.start_action(self.next_action)
        self.next_action = None
