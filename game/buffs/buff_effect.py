
class BuffEffect:
    def __init__(self):
        pass
    
    def apply(self, buff):
        """Optionally return a state value/object"""
        return None
    
    def update(self, buff, state):
        """Optionally return a state value/object"""
        return state
    
    def remove(self, buff, state):
        pass