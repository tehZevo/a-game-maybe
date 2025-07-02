from game.items.defs import Staff
from game.items import EquipGrade as G
from game.items import Rarity as R
import game.data.skills as S

wooden_staff = Staff(
    id="wooden_shortsword",
    grade=G.E,
    icon="assets/items/weapons/staffs/wooden_staff.png"
)

staff_of_healing = Staff(
    id="staff_of_healing",
    grade=G.D,
    rarity=R.EPIC,
    icon="assets/items/weapons/staffs/staff_of_healing.png",
    attack_skill=S.heal
)
