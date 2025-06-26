
def get_item(id):
    import game.data.items as items
    return getattr(items, id)

def get_sprite(id):
    import game.data.sprites as sprites
    return getattr(sprites, id)

def get_map(id):
    import game.data.maps as maps
    return getattr(maps, id)

def get_buff(id):
    import game.data.buffs as buffs
    return getattr(buffs, id)

def get_mob(id):
    import game.data.mobs as mobs
    return getattr(mobs, id)

def get_skill(id):
    import game.data.skills as skills
    return getattr(skills, id)