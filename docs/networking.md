# Networking
* Event-based
* Both the client and the server have their own game world
* Networking capabilities are broken up into their own components, eg:
  * PositionNetworking is responsible for sending PositionUpdated events
  * DespawnNetworking is responsible for sending EntityDespawned events

## `Client`
* Can register `EventHandler`s

## `Server`
* Can register `CommandHandler`s

## `Command`s
* Are sent from the client to the server

## `Event`s
* Are sent from the server to the client

## `CommandHandler`s
* Handle commands
* Receive the client's id alongside the command

## `EventHandler`s
* Handle events

## `Id` component
* Stores an entity id for client/server syncing

## Commands
* PlayerMove: move the player

## Events
* PlayerAssigned: Sent when a player connects, tells the player which actor they control
* ActorSpawned: Sent when an actor is created on the server (currently only when a player connects)
* PositionUpdated: Sent to update a client side entity position
* TilesetUpdated: Sends a tileset to the client
