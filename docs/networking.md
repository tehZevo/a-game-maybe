# Networking
* Event-based
* Both the client and the server have their own game world

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
