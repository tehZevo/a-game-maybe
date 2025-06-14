import random

from game.ecs import Component
from game.actions import Move, UseSkill
from game.utils import Vector
from game.utils.teams import ENEMY
import game.components as C

class Enemy(Component):
  def __init__(self, mobdef):
    super().__init__()
    self.require(C.Actor)
    self.target_distance = 5
    self.follow_dist = 2
    self.target = None
    self.mobdef = mobdef

  def start(self):
    #make enemies 1/4 base player speed
    self.get_component(C.Stats).move_speed_multiplier = 0.25
    if self.mobdef.sprite is not None:
      self.get_component(C.Sprite).set_sprite(self.mobdef.sprite)
    self.get_component(C.Team).team = ENEMY

  def on_destroy(self):
    #drop items
    dropper = self.get_component(C.ItemDropper)
    pos = self.get_component(C.Position).pos
    #chance to drop each item based on its drop rate
    for item in self.mobdef.drops:
      if random.random() < item.calc_drop_rate():
        dropper.drop(item, pos)

  def update(self):
    move_dir = Vector()
    enemy_pos = self.get_component(C.Position).pos

    #TODO: make this a behavior and put skill in equips in mobdef

    #find player to target
    #TODO: find anything on team we are not friends with
    if self.target is None:
      for player in self.entity.world.find(C.Player):
        #calc distance
        player_pos = player.get_component(C.Position).pos
        dist = player_pos.distance(enemy_pos)
        if dist < self.target_distance:
          self.target = player
          break

    #follow and use skills
    if self.target is not None:
      if not self.target.alive:
        self.target = None
      else:
        target_pos = self.target.get_component(C.Position).pos
        dist = target_pos.distance(enemy_pos)
        if dist < self.follow_dist:
          skill = random.choice(self.mobdef.skills)
          self.get_component(C.Actor).act(UseSkill(skill))
        else:
          move_dir = target_pos - enemy_pos

        #apply move action
        self.get_component(C.Actor).act(Move(move_dir))

    #TODO: add wandering behavior
