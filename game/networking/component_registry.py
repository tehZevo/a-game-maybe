def get_component_classes():
  from ..components.actor import Actor, Enemy, Invulnerable, Player, Stats
  from ..components.core import DungeonFloor, Interactable
  from ..components.graphics import Sprite
  from ..components.item import DroppedItem
  from ..components.particles import ParticleEmitter
  from ..components.physics import Position, Rect, Physics
  from ..components.tiles import Stairs

  return locals()
