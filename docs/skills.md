# Skill System

## `SkillEffect`s
* Contain logic for individual effects of a skill, eg:
  * Targeting
  * Damage
  * Restoring hp/mp
  * Applying force
* Some skill effects accept a list of children, such as target effects, which will provide each child skill effect with a target

## `SkillDef`
* Wraps a list of skill effects
* Has additional fields for the use of a skill (hp/mp cost, cast time, etc)

## `Skill` component
* An instance of a skill effect in the game world
