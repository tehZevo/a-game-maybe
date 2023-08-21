
class StatsListener:
  def __init__(self):
    pass

  def on_stats_changed(self, stats):
    raise NotImplementedError
