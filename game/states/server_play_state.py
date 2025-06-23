from game.ecs import World
from game.constants import FPS, DT
import game.networking.commands as commands
import game.components as C
import game.networking.events as E
import game.data.maps as M

#TODO: maybe move things like player entity map here?
class ServerPlayState:
  def __init__(self, room, mapdef, channel):
    #TODO: store save data at room level
    self.room = room
    self.channel = channel
    self.channel.setup_handlers([
      commands.PlayerMoveHandler(self),
      commands.PlayerUseSkillHandler(self),
      commands.PlayerInteractHandler(self),
      commands.SyncHandler(self, self.room.save_data),
      commands.ReportPositionHandler(self),
      commands.ReportVelocityHandler(self),
    ])

    self.world = self.generate_world(mapdef)
    self.server_manager = self.world.find_component(C.ServerManager)

    print("[Server] Hello play state")

  def on_disconnect(self, client_id):
    self.server_manager.player_unregister(client_id)
  
  def generate_world(self, mapdef):
    #create new world
    world = World()
    world.create_entity([C.GameMaster(self, mapdef)])
    world.create_entity([C.DroppedItemManager()])
    
    #add server manager
    server_manager = C.ServerManager()
    world.create_entity([server_manager])
    #TODO: rename to channel
    server_manager.server = self.channel

    #generate using mapdef
    mapdef.generator.generate(world, mapdef)
    
    return world

  def transition(self, mapdef):
    #TODO: make whatever called this call room.transition
    world = self.generate_world(mapdef)
    #TODO: broadcast_synced?
    #TODO: room should send worldclosed instead
    self.server.broadcast(E.WorldClosed())
  
  def save(self, save_data):
    """Sync relevant world data to room save data"""
    for client_id in self.save_data.player_data.keys():
      entity_id = self.server_manager.player_entity_map[client_id]
      ent = self.server_manager.networked_entities[entity_id]
      save_data.save_player_data(client_id, ent)
  
  def step(self):
    self.channel.handle_commands()
    self.world.update()
