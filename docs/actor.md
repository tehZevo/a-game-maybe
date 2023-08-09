# Actor system

## Actors (`Actor` component)
* Are entities which can take actions
* Have stats
* Can use skills (via `UseSkill` action)
* Can move around
* Can drop items (via `ItemDropper` component)
* Have an equip inventory
* Have a team
* Has an active action and a next action (the "buffered" action), which will be used upon completion of the current action

## `Action`s
* Can be interrupted
* Can reference the actor to manipulate it during the course of the action
