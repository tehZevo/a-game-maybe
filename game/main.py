from .game import Game

#handling teams:
#TODO: idea for how to handle:
# TeamManager entity
# enemies assign their Team component the value "enemy" (or some other team), and players get "player", etc
# TeamManager has a mapping of teams to their disposition (ally, enemy, neutral)
# target effects then query the team manager and filter entities with a given Team (component)

#TODO: target effects should have a selection order (nearest/random)

#TODO: networking
#- commands: sent from client to server
#- events: sent from server to client
#- server has an ECS with a Server entity (or one per player?) to determine what events to send
#- client has its own ECS with a Client entity (receives events and takes the appropriate action (creating ents/components, etc))
#- client and server likely have separate components (eg client may have a "dummy physics" that just interpolates physics from server)

#TODO: refactor skill effect targets to be a component on the skill entity
#TODO: refactor skill effects to not store state
#TODO: add "target type" to target skill effects to avoid referencing player/enemy in skills themselves and to make skills user agnostic

#TODO: fix items getting stuck to player on pickup

#TODO: cache component -> entity mapping so we can find entities in constant time
#TODO: make it so target effects require LOS (flag?)
#TODO: damage hits (basically a delay+repeat of damage)
#TODO: add invulnerability animation
#TODO: icon ui component to draw equips and skills
#TODO: make ui components mountable to screen corners/edges and then use position as an offset
#TODO: use drawable in renderer
#TODO: improve collisions (remove small pixel gap on bottom/right collisions)
#TODO: make collision debug drawing
#TODO: merge solid tile rects greedily
#TODO: knock back enemy if you do more than 10% of its hp?
#TODO: make it possible to buffer a "face direction" between skills
# does this mean allowing skills to be used in a certain direction?
#TODO: maybe make direction component for tileentity facing direction
# how to handle fine-grained direction for actor though? is that even needed?
#TODO: fix game slowing down after some time (fixes itself when moving dungeon floors, might be caused by enemies attacking player; leak?)
# also remidied by killing enemies
#TODO: make +y up
#TODO: ECS for particles so i can separate out particle behaviors
#TODO: reduce delay on interact (will require handling key pressed events so player cant hold to repeatedly interact)
#TODO: fix subpixel glitchiness
#TODO: make 0, 0 center of sprites
#TODO: box camera
#TODO: add ysorting to camera
#TODO: generator should make a player spawn point component, which players are spawned on by the generators spawn method
#TODO: gold, health, mana drops: walk over them to pick them up
#TODO: maybe distinction between world sprite and ui sprite
#TODO: skill idea: "ally bomb" (or something like that): damage enemies nearby allies (target allies, then target enemies)
#TODO: make targets have a filter type: "enemies" or "allies" or "self"? idk
#TODO: distance based delay effect (delay in seconds per unit)
#TODO: ranged attacks will feel nicer with a bit of delay (think magic claw from maple story)


Game().run()
