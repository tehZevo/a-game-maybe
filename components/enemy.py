import random

from ecs import Component
from components import Actor, Stats, Position, Sprite, ItemDropper
from components.items import Hat, Armor
from actions import Move
from utils import Vector

class Enemy(Component):
  def __init__(self):
    super().__init__()
    self.require(Actor)
    self.target_distance = 5
    self.target = None
    self.drops = [Hat, Armor]
    self.drop_rate = 0.25

  def start(self):
    #TODO: hack for making enemy slower than player
    self.get_component(Stats).move_speed = 50
    self.get_component(Sprite).set_sprite("assets/enemy.png")

  def on_destroy(self):
    #drop item
    dropper = self.get_component(ItemDropper)
    pos = self.get_component(Position).pos
    if random.random() < self.drop_rate:
      item = random.choice(self.drops)
      dropper.drop(item, pos)

  def update(self):
    #TODO: meh, dodging circular import
    from components import Player

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

    if self.target is not None:
      target_pos = self.target.get_component(Position).pos
      move_dir = target_pos - enemy_pos

      #apply move action
      self.get_component(Actor).act(Move(move_dir))

    #TODO: add wandering behavior
