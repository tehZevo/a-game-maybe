# Entity-Component System
*Not to be confused with an entity-component-system system*

## `World`
* A collection of `Entity`s
* Calls each's `Entity`'s `start` and `update` methods

## `Entity`
* A collection of `Component`s
* Calls each `Component`'s `start` and `update` methods

## `Component`
* A Unity-style "heavyweight" component that contains data as well as game logic
