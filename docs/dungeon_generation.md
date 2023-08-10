# Dungeon Generation

## `FloorGenerator`s
* Have a `generate` method, which should be impl'd to populate a `world`

## `Tileset`
* Has a fixed width and height
* Holds tiles

## `Tile`
* Has an image path and a `solid` flag

## `BakedTileset`
* Draws all `Tileset`'s `Tile`s' images onto a single Pygame `Surface`
* Creates collision Pygame `Rect`s
