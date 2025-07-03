from game.ecs import Component
import game.components as C

from ..networking.networking import Networking
from game.utils import Vector, Direction, vector_to_direction
import game.networking.events as E
import game.actions as A
from game.constants import DT
from game.graphics import DamageNumberType

class Actor(Component):
  def __init__(self):
    super().__init__()
    self.require(C.Physics, C.Sprite, C.Stats, C.ItemDropper, C.Equips, \
      C.Collisions, C.Buffs, C.Team, C.Networking, C.ActorNetworking)
    self.action = None
    self.next_action = None
    self.look_dir = Vector(0, -1)
    self.move_dir = self.look_dir.copy()
    self.actor_alive = True
    self.shadow = None
    self.skill_cooldowns = {}

  def start(self):
    self.shadow = self.entity.world.create_entity([
      C.Position(self.entity[C.Position].pos.copy()),
      C.Shadow()
    ])
    
  def damage(self, amount):
    amount = int(amount)
    stats = self.get_component(C.Stats)
    stats.add_hp(-amount)

    #find all damage listeners and call their on_damage
    for listener in self.entity.find(C.DamageListener):
      #TODO: track source
      source = None
      listener.on_damage(source, amount)
    
    server_manager = self.entity.world.find_component(C.ServerManager)
    networking = self.entity[C.Networking]
    if server_manager is not None:
      event = E.ActorDamaged(networking.id, DamageNumberType.NORMAL, amount)
      networking.broadcast_synced(event)
  
  def heal(self, amount):
    #TODO: track source
    stats = self.get_component(C.Stats)
    stats.add_hp(amount)

    server_manager = self.entity.world.find_component(C.ServerManager)
    networking = self.entity[C.Networking]
    if server_manager is not None:
      event = E.ActorDamaged(networking.id, DamageNumberType.HEAL, amount)
      networking.broadcast_synced(event)
  
  def heal_mp(self, amount): 
    #TODO: send actor damaged?
    stats = self.get_component(C.Stats)
    stats.add_mp(amount)

  #TODO: maybe move to equips or skillset
  def use_skill_in_slot(self, slot):
    skill_item = self.get_component(C.Equips).skills[slot]
    skilldef = skill_item and skill_item.skilldef
    if skilldef is None:
      return

    if skilldef.id in self.skill_cooldowns:
      return
    
    if skilldef.cooldown is not None:
      self.skill_cooldowns[skilldef.id] = skilldef.cooldown
    
    self.act(A.UseSkill(skill_item.skilldef))

  def start_action(self, action):
    #TODO: use decorator or something
    server_manager = self.entity.world.find_component(C.ServerManager)
    networking = self.entity[C.Networking]
    if server_manager is not None:
      event = E.ActionStarted(networking.id, action.__class__.__name__, action.serialize())
      networking.broadcast_synced(event)

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
        
        #TODO: use decorator or something
        server_manager = self.entity.world.find_component(C.ServerManager)
        networking = self.entity[C.Networking]
        if server_manager is not None:
          event = E.ActionEnded(networking.id)
          networking.broadcast_synced(event)
        self.action = None

    #start new action if old action is finished
    if self.action is None and self.next_action is not None:
      a = self.next_action
      self.next_action = None
      self.start_action(a)

  def update(self):
    stats = self.get_component(C.Stats)
    pos = self.get_component(C.Position)
    self.shadow[C.Position].pos = pos.pos.copy()

    for id, cd in self.skill_cooldowns.items():
      self.skill_cooldowns[id] -= DT
    
    self.skill_cooldowns = {k: v for k, v in self.skill_cooldowns.items() if v > 0}
    
    if self.actor_alive and stats.hp <= 0:
      self.actor_alive = False
      for listener in self.entity.find(C.DeathListener):
        listener.on_death()
      return

    if not self.actor_alive:
      return

    self.update_action()

  def on_destroy(self):
    self.shadow.remove()