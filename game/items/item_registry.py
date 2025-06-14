
def get_item(id):
    import game.data.items as items
    return getattr(items, id)
