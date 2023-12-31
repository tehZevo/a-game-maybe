- teleporters
- player spawn tile entity
- network floor transitions
  - add ability to spawn entities for a certain player
    - call this method on player join for all entities
- add "spawn" to network behaviors, which should generate a list of events that should be broadcast/sent to player upon spawn
- air mechanics
  - jumping
  - shadow (separate entity?)
  - skills that can only be used midair
  - skills that cannot be used midair
- fix sprites sometimes being black
  - i think this is due to component ordering when reconstructing on the client
- make client ui target client's player
- fix skill use generating tons of stats updated events
 - maybe store stat updates per game tick and then send one StatsUpdated on the next tick>
- network particle emitters
- spawn networked players with player data when loading new world
- use eventcatalog to document events?
- client side prediction :^)
- make Networked component handle its own spawning (and despawning) on the clients?
- split project into client, server, and common packages
- player radius/visibility spawning/despawning/updates
  - when player enters radius, spawn entity
  - as long as player is within radius, send updates
  - when player exits radius, despawn entity
  - might be useful to keep track of entities that can be seen by each player in the server manager
- don't sync position every tick, interpolate
- sync velocity
- greedily merge walls when creating tilesetphysics rects
- target effects should have a selection order (nearest/random)
- refactor skill effect targets to be a component on the skill entity
- refactor skill effects to not store state
- fix items getting stuck to player on pickup
- cache component -> entity mapping so we can find entities in constant time
- make it so target effects require LOS (flag?)
- damage hits (basically a delay+repeat of damage)
- add invulnerability animation
- icon ui component to draw equips and skills
- make ui components mountable to screen corners/edges and then use position as an offset
- use drawable in renderer
- improve collisions
  - remove small pixel gap on bottom/right collisions
  - fix passing through walls at high speeds
- make collision debug drawing
- knock back enemy if you do more than 10% of its hp?
- make it possible to buffer a "face direction" between skills
  - does this mean allowing skills to be used in a certain direction?
- maybe make direction component for tileentity facing direction
  - how to handle fine-grained direction for actor though? is that even needed?
- make +y up
- separate ECS for particles so they dont slow down main world queries
  - add tileset physics to this world so we can have particles bounce off walls, etc
- reduce delay on interact (will require handling key pressed events so player cant hold to repeatedly interact)
- fix subpixel glitchiness
- make 0, 0 center of sprites
- box camera
- add ysorting to camera
- generator should make a player spawn point component, which players are spawned on by the generators spawn method
- gold, health, mana drops: walk over them to pick them up
- maybe distinction between world sprite and ui sprite
- skill idea: "ally bomb" (or something like that): damage enemies nearby allies (target allies, then target enemies)
- distance based delay effect (delay in seconds per unit)
- ranged attacks will feel nicer with a bit of delay (think magic claw from maple story)
