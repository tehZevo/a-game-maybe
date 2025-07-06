from game.items.defs import Hat, Suit, Gloves, Shoes
from game.items import EquipGrade as G
from game.stats import equip_stats_calculator as EC

def create_set(prefix, grade, primary_archetype):
  kw = {
    "grade": grade,
    "primary_archetype": primary_archetype,
    "equip_archetype": EC.cloth,
  }
  hat = Hat(
    id=f"{prefix}_hat",
    icon=f"assets/items/armor/cloth/{prefix}_hat.png",
    **kw
  )
  robe = Suit(
    id=f"{prefix}_robe",
    icon=f"assets/items/armor/cloth/{prefix}_robe.png",
    **kw
  )
  gloves = Gloves(
    id=f"{prefix}_gloves",
    icon=f"assets/items/armor/cloth/{prefix}_gloves.png",
    **kw
  )
  shoes = Shoes(
    id=f"{prefix}_shoes",
    icon=f"assets/items/armor/cloth/{prefix}_shoes.png",
    **kw
  )
  return hat, robe, gloves, shoes

cotton_hat, cotton_robe, cotton_gloves, cotton_shoes = create_set("cotton", G.E, EC.cloth_int)
linen_hat, linen_robe, linen_gloves, linen_shoes = create_set("linen", G.D, EC.cloth_wis)