from game.ecs import Component
from ..physics import Physics, Collisions
from ..graphics import Sprite
from ..item import ItemDropper, Equips
from ..teams import Team
from . import Stats, DamageListener
from game.utils import Vector

class Actor(Component):
  def __init__(self):
    super().__init__()
    #TODO: circular import
    from ..networking import ActorNetworking
    self.require(Physics)
    self.require(Sprite)
    self.require(Stats)
    self.require(ItemDropper)
    self.require(Equips)
    self.require(Collisions)
    self.require(Team)
    self.require(ActorNetworking)
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

  #TODO: maybe move to equips or skillset
  def use_skill_in_slot(self, slot):
    #TODO: circular reference
    from game.actions import UseSkill
    skill_item = self.get_component(Equips).skills[slot]
    if skill_item is None:
      print("warning: tried to use None skill in slot", slot)
      return

    self.act(UseSkill(skill_item.skilldef))

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

      if not self.action.active:
        self.action = None

    #start new action if old action is finished
    if self.action is None and self.next_action is not None:
      a = self.next_action
      self.next_action = None
      self.start_action(a)
