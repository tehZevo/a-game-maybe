from game import Game

#TODO: top level skill wrapper that defines things like use delay
#TODO: ECS for particles so i can separate out particle behaviors
#TODO: collisions
#TODO: reduce delay on interact (will require handling key pressed events so player cant hold to repeatedly interact)
#TODO: fix subpixel glitchiness
#TODO: make 0, 0 center of sprites
#TODO: box camera
#TODO: use pygame vector https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
#TODO: add ysorting to camera
#TODO: make interactible interface for components
#TODO: need to create new player anyway... that way he has a reference to the new world
#TODO: generator should make a player spawn point component, which players are spawned on by the generators spawn method
#TODO: use movespeed from stats
#TODO: persist player data across floors
#TODO: gold, health, mana drops: walk over them to pick them up
#TODO: maybe distinction between world sprite and ui sprite
#TODO: skill idea: "ally bomb" (or something like that): damage enemies nearby allies (target allies, then target enemies)
#TODO: make targets have a filter type: "enemies" or "allies" or "self"? idk
#TODO: distance based delay effect (delay in seconds per unit)
#TODO: ranged attacks will feel nicer with a bit of delay (think magic claw from maple story)
#TODO: concept of "teams" so player skill effects automatically target enemies (and vice versa)

Game().run()
