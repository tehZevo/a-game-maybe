# Buffs
`Buffdef`s contain `BuffEffect`s

`BuffEffect`s are stateless but can create a custom state value/object in apply. That state is then passed to (and returned from) subsequent calls to update and remove.

`Buff`s are instances of buffdefs that contain the calculated power/time and state of the buff. `Buff`s are unique per `BuffDef` type in an actor's `Buffs`.

`Buffs` is a component that stores an actor's `Buff`s.