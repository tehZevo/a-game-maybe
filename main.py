# /// script
# dependencies = [
#  "pygame",
#  "dacite",
# ]
# ///

#pygbag entrypoint
import game.run_local
# TODO: doesnt work.. get:
#AttributeError: 'Lock' object has no attribute '_at_fork_reinit'
#at     reader, writer = await asyncio.open_connection(self.host, self.port)
# import game.run_web_networked
