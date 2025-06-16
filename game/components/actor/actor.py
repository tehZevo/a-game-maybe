from game.ecs import Component
import game.components as C

from ..networking.networking import Networking
from game.utils import Vector

class Actor(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Physics, C.Sprite, C.Stats, C.ItemDropper, C.Equips, \
      C.Collisions, C.Team, C.Networking, C.ActorNetworking)
    self.action = None
    self.next_action = None
    self.look_dir = Vector(0, -1)
    self.actor_alive = True

  def damage(self, amount):
    stats = self.get_component(C.Stats)
    stats.add_hp(-amount)

    #find all damage listeners and call their on_damage
    for listener in self.entity.find(C.DamageListener):
      #TODO: add source
      source = None
      listener.on_damage(source)

  #TODO: maybe move to equips or skillset
  def use_skill_in_slot(self, slot):
    from game.actions import UseSkill
    skill_item = self.get_component(C.Equips).skills[slot]
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

  def update_action(self):
    sprite = self.get_component(C.Sprite)
    #update current action
    if self.action is not None:
      self.action.update()

      if not self.action.active:
        if self.next_action is None:
          #TODO: maybe we need a listener for this so player can set his animation between actions or w/e
          #TODO: need better place to set/control animations
          sprite.set_animation("idle")
        self.action = None

    #start new action if old action is finished
    if self.action is None and self.next_action is not None:
      a = self.next_action
      self.next_action = None
      self.start_action(a)

  def update(self):
    stats = self.get_component(C.Stats)
    
    if self.actor_alive and stats.hp <= 0:
      self.actor_alive = False
      for listener in self.entity.find(C.DeathListener):
        listener.on_death()
      return

    if not self.actor_alive:
      return

    self.update_action()
