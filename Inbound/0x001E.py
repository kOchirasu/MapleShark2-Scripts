from script_api import *
from common import *

# <A HREF="event:itemTooltip,2867553202885834708,3,2867553202885834708,20000004,1">[Elixir]</A>
AddInt("Unknown") # 1
AddLong("ItemUid")
id = AddInt("ItemId")
AddInt("Rarity?")
DecodeItem(id)
