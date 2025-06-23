import sys
from collections import defaultdict

import pygame

from game.ecs import World
import game.components as C
import game.networking.events as E
import game.networking.commands as commands
from game.utils import Vector

class ClientPlayState:
  def __init__(self, game, channel):
    self.channel = channel
    self.game = game
    self.channel.setup_handlers([
      E.PlayerAssignedHandler(self),
      E.TilesetUpdatedHandler(self),
      E.ChunkLoadedHandler(self),
      E.ChunkUnloadedHandler(self),
      E.EntitySpawnedHandler(self),
      E.PositionUpdatedHandler(self),
      E.VelocityUpdatedHandler(self),
      E.SpriteChangedHandler(self),
      E.IconChangedHandler(self),
      E.ParticleEmitterUpdatedHandler(self),
      E.EntityDespawnedHandler(self),
      E.MobUpdatedHandler(self),
      E.StatsUpdatedHandler(self),
      E.EquipsUpdatedHandler(self),
      E.BuffsUpdatedHandler(self),
    ])
    
    #create ui world and manager
    self.ui_world = World()
    self.hud = self.ui_world.create_entity([C.HUD()])

    self.ui_renderer = self.ui_world.create_entity([
      C.Renderer(self.game.render_width, self.game.render_height)
    ])

    self.world = World()
    self.init_world()

    self.channel.send(commands.HelloWorld())

  def init_world(self):
    #setup client world
    self.world.create_entity([C.GameMaster(self, None)]) #NOTE: we'll set mapdef when we get it from the server
    self.camera = self.world.create_entity([C.Camera()])
    self.renderer = self.world.create_entity([
      C.WorldRenderer(self.game.render_width, self.game.render_height, self.camera)
    ])
    self.world.create_entity([C.TileRendering()])
    self.world.create_entity([C.TilePhysics()])
    self.particle_system = self.world.create_entity([C.ParticleSystem()])
    
    self.client_manager = C.ClientManager()
    #TODO: remove and just use reference to state
    self.client_manager.client = self.channel
    self.world.create_entity([self.client_manager])

    #set hud world and player
    hud_comp = self.hud.get_component(C.HUD)
    hud_comp.game_world = self.world

  def step(self, pressed, held, released):
    self.channel.handle_events()

    for key_handler in self.ui_world.find_components(C.KeyHandler):
      key_handler.handle_keys(pressed, held, released)
    for key_handler in self.world.find_components(C.KeyHandler):
      key_handler.handle_keys(pressed, held, released)

    #update world
    self.world.update()

    #render
    self.game.screen.fill((0, 0, 0))
    self.renderer.get_component(C.Renderer).render(self.game.screen)

    #draw UI
    self.ui_world.update()
    self.ui_renderer.get_component(C.Renderer).render(self.game.screen)