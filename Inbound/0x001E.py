from script_api import *
from common import *

# <A HREF="event:itemTooltip,2867553202885834708,3,2867553202885834708,20000004,1">[Elixir]</A>
add_int("Unknown") # 1
add_long("ItemUid")
id = add_int("ItemId")
add_int("Rarity?")
decode_item(id)
