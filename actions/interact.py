from components import Position, Interactable
from actions import Action
from utils.constants import DT
from utils.find_in_range import find_in_range

INTERACT_RADIUS = 1

#TODO: refactor to add interactible interface and just interact with one entity's components

class Interact(Action):
  def __init__(self):
    super().__init__()
    self.interruptible = False
    self.active = True
    self.use_time = 0.5

  def start(self):
    entity_pos = self.entity.get_component(Position).pos

    interactables = find_in_range(self.entity.world, Interactable, entity_pos, INTERACT_RADIUS)
    for interactable in interactables:
      for component in interactable.components.values():
        if issubclass(component.__class__, Interactable):
          component.interact(self.entity)

    # #find staircases
    # #TODO
    # staircases = find_in_range(self.entity.world, Stairs, entity_pos, INTERACT_RADIUS)
    # if len(staircases) > 0:
    #   stairs = staircases[0].get_component(Stairs)
    #   #TODO: how do we "escape" ecs so that we can
    #   # set the world of the engine and transition to a new floor?
    #   # we could have a worldspawn like entity?
    #


  def update(self):
    self.use_time -= DT
    if self.use_time <= 0:
      self.active = False
