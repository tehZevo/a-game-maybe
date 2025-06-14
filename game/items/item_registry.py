
def get_item(id):
    import game.items as items
    return getattr(items, id)
