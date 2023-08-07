from game import Game

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
#TODO: camera
#TODO: concept of "teams" so player skill effects automatically target enemies (and vice versa)

Game().run()
