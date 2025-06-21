import random

from game.ecs import Component
import game.actions as A
from game.utils import Vector
from game.utils.teams import ENEMY
from game.components.actor import DeathListener, DamageListener
import game.components as C
from game.utils.constants import ENEMY_MOVE_SPEED, DT
from game.components.networking import NetworkBehavior
import game.networking.events as E

#TODO: constants?
MOVE_UPDATE_TIME = 1
MOVE_DIST_THRESH = 0.5

#TODO: rename to Mob?
class Enemy(Component, NetworkBehavior, DeathListener, DamageListener):
  def __init__(self, mobdef=None):
    super().__init__()
    self.require(C.Actor)
    #TODO: make constants
    self.target_distance = 5
    #TODO: base on skill (add advertised target range to skilldef)
    self.attack_dist = 2
    self.target = None
    self.last_move_update_time = 0
    self.move_pos = None
    self.mobdef = mobdef

  def start(self):
    self.entity[C.Stats].move_speed_multiplier = ENEMY_MOVE_SPEED
    self.entity[C.Team].team = ENEMY
    if self.mobdef and self.mobdef.sprite:
      self.entity[C.Sprite].set_sprite(self.mobdef.sprite)
  
  def on_damage(self, attacker, amount):
    pass
    #TODO:
    # self.entity.world.create_entity([
    #   C.Position(self.entity[C.Position].pos.copy()),
    #   C.DamageNumber(amount, stack=0, delay=0)
    # ])

  def on_death(self):
    #TODO: bad guard
    is_server = self.entity.world.find_component(C.ServerManager)
    if not is_server:
      return
    #drop items
    dropper = self.get_component(C.ItemDropper)
    pos = self.get_component(C.Position).pos
    #chance to drop each item based on its drop rate
    for item in self.mobdef.drops:
      if random.random() < item.calc_drop_rate():
        dropper.drop(item, pos)
    #TODO: play animation then die
    self.entity.remove()

  def find_target(self):
    my_pos = self.entity[C.Position].pos
    #TODO: find anything on team we are not friends with
    for player in self.entity.world.find(C.Player):
      #calc distance
      player_pos = player[C.Position].pos
      dist = player_pos.distance(my_pos)
      if dist < self.target_distance:
        self.target = player
        return

  def mob_event(self, networking):
    return E.MobUpdated(networking.id, self.mobdef.id, self.move_pos)

  def on_client_join(self, networking, client_id):
    networking.send_to_client(client_id, self.mob_event(networking))
  
  def on_start_server(self, networking):
    networking.broadcast_synced(client_id, self.mob_event(networking))

  def update_move_pos(self):
    net = self.entity[C.Networking]
    if self.move_pos is not None and self.target is None:
      self.move_pos = None
      self.last_move_update_time = 0
      net.broadcast_synced(self.mob_event(net))
      return
    
    self.last_move_update_time += DT
    if self.last_move_update_time >= MOVE_UPDATE_TIME:
      self.last_move_update_time = 0
      self.move_pos = self.target[C.Position].pos
      net.broadcast_synced(self.mob_event(net))
  
  def update_sprite(self, move_dir):
    if move_dir.x < 0:
      self.entity[C.Sprite].flip_x = True
    elif move_dir.x > 0:
      self.entity[C.Sprite].flip_x = False
      
  def update(self):
    if self.move_pos is None:
      #TODO: don't keep updating this
      self.entity[C.Actor].act(A.Move(None))
      return
    
    my_pos = self.entity[C.Position].pos
    dist = my_pos.distance(self.move_pos)
    if dist > MOVE_DIST_THRESH:
      move_dir = (self.move_pos - my_pos).normalized()
      #TODO: updating sprite on the client feels weird
      self.update_sprite(move_dir)
      #TODO: MoveTo action?
      self.entity[C.Actor].act(A.Move(move_dir))

  def update_server(self, networking):
    enemy_pos = self.get_component(C.Position).pos

    #TODO: make this a behavior and put skill in equips in mobdef
    #TODO: add wandering behavior

    if self.target is None:
      self.find_target()
      return

    if not self.target.alive:
      self.target = None
      return
    
    #follow and use skills
    self.update_move_pos()

    target_pos = self.target[C.Position].pos
    dist = target_pos.distance(enemy_pos)
    if dist < self.attack_dist:
      skill = random.choice(self.mobdef.skills)
      self.move_pos = None
      self.get_component(C.Actor).act(A.UseSkill(skill))
      networking.broadcast_synced(self.mob_event(networking))

