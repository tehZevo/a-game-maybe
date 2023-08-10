import random

from ecs import Component
from components.actor.actor import Actor
from components.actor.stats import Stats
from components.physics.position import Position
from components.graphics.sprite import Sprite
from components.item.item_dropper import ItemDropper
from components.teams.team import Team
from items import Hat, SkillItem
from actions import Move, UseSkill
from utils import Vector
from utils.teams import ENEMY

class Enemy(Component):
  def __init__(self):
    super().__init__()
    #TODO: reee
    from skills.test_alpha_skill import test_alpha_skill

    self.require(Actor)
    self.target_distance = 5
    self.target = None
    #drops are instantiated here, and have a drop_rate chance of dropping each
    #TODO: store this in a "inventory" (which can be shared with chest tileentity)?
    self.drops = [Hat(), SkillItem(test_alpha_skill)]
    self.follow_dist = 2
    #TODO: reee
    from skills.test_enemy_skill import test_enemy_skill
    self.skill = test_enemy_skill

  def start(self):
    #make enemies 1/4 base player speed
    self.get_component(Stats).move_speed_multiplier = 0.25
    self.get_component(Sprite).set_sprite("assets/enemy.png")
    self.get_component(Team).team = ENEMY

  def on_destroy(self):
    #drop items
    dropper = self.get_component(ItemDropper)
    pos = self.get_component(Position).pos
    #chance to drop each item based on its drop rate
    for item in self.drops:
      if random.random() < item.drop_rate:
        dropper.drop(item, pos)

  def update(self):
    #TODO: meh, dodging circular import
    from components.actor.player import Player

    move_dir = Vector()
    enemy_pos = self.get_component(Position).pos

    #find player
    players = self.entity.world.find(Player)
    player = None if len(players) == 0 else players[0]

    if self.target is None and player is not None:
      #calc distance
      player_pos = player.get_component(Position).pos
      dist = player_pos.distance(enemy_pos)
      if dist < self.target_distance:
        self.target = player

    #follow and use skills
    if self.target is not None:
      target_pos = self.target.get_component(Position).pos
      dist = target_pos.distance(enemy_pos)
      if dist < self.follow_dist:
        self.get_component(Actor).act(UseSkill(self.skill))
      else:
        move_dir = target_pos - enemy_pos

      #apply move action
      self.get_component(Actor).act(Move(move_dir))

    #TODO: add wandering behavior
