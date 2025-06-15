
def get_item(id):
    import game.data.items as items
    return getattr(items, id)

def get_sprite(id):
    import game.data.sprites as sprites
    return getattr(sprites, id)

def get_map(id):
    import game.data.maps as maps
    return getattr(maps, id)