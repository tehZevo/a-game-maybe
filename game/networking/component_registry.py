#TODO: replace this with C.__dict__
def get_component_classes():
  from ..components.actor import Actor, Enemy, Invulnerable, Player, Stats, \
    ActorNetworking, StatsSyncing, EquipsSyncing, BuffsSyncing
  from ..components.core import Interactable
  from ..components.graphics import Sprite, SpriteSyncing, Icon, IconSyncing
  from ..components.item import DroppedItem
  from ..components.particles import ParticleEmitter
  from ..components.physics import Position, Rect, Physics, PositionSyncing
  from ..components.tiles import ChunkNetworking

  return locals()
