import game.components as C

from game.utils import Vector
from .screen import Screen

class TextInputScreen(Screen):
  def __init__(self, on_submit, default_text=None, label="Input:", draw_length=20, max_length=None):
    super().__init__()
    self.on_submit = on_submit
    #TODO: use
    self.label = label
    #TODO: meh
    self.ui_manager = None
    self.draw_length = draw_length
    self.max_length = max_length
    self.default_text = default_text
  
  def handle_submit(self, text):
    self.on_submit(text)
    self.text_field.remove()
    self.entity.remove()
  
  def on_destroy(self):
    self.ui_manager.pop()

  def start(self):
    self.text_field = self.entity.world.create_entity([
      C.Position(Vector(32, 32)),
      C.TextField(
        self.handle_submit,
        text=self.default_text,
        draw_length=self.draw_length,
        max_length=self.max_length
      )
    ])

  def handle_keys(self, kb):
    self.text_field[C.TextField].handle_keys(kb)