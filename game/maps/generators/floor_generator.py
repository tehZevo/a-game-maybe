from game.maps.chunk_tiles import chunk_tiles
import game.components as C

class FloorGenerator:
  def __init__(self):
    pass

  def generate(self, mapdef):
    """Override me and return (tiles, entities)"""
    return NotImplementedError

  def populate_world(self, world, mapdef):
    tiles, entities = self.generate(mapdef)
    
    chunks = chunk_tiles(tiles)
    world.create_entity([C.TilePhysics(chunks)])
    world.create_entity([C.ChunkNetworking(chunks)])

    for comps in entities:
      world.create_entity(comps)