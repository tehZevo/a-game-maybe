from subprocess import Popen

commands = [
  "python -m game.run_server",
  "python -m game.run_client",
]
procs = [Popen(e) for e in commands]

for p in procs:
  p.wait()
