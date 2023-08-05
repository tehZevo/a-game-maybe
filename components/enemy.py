from ecs import Component
from components import Actor, Player, Stats, Position
from actions import Move
from utils import Vector

class Enemy(Component):
  def __init__(self):
    super().__init__()
    self.require(Actor)

  def init(self):
    #TODO: hack for making enemy slower than player
    self.get_component(Stats).move_speed = 0.5

  def update(self):
    move_dir = Vector()

    #move towards player
    players = self.entity.world.find(Player)
    player = None if len(players) == 0 else players[0]

    if player is not None:
      #TODO: return vector from get_pos
      player_pos = Vector(*player.get_component(Position).get_pos())
      enemy_pos = Vector(*self.get_component(Position).get_pos())
      move_dir = player_pos - enemy_pos

    #apply move action
    self.get_component(Actor).act(Move(move_dir))
