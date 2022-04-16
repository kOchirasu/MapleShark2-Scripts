''' MESSENGER_BROWSER '''
from script_api import *
from item import *

# <A HREF="event:itemTooltip,2867553202885834708,3,2867553202885834708,20000004,1">[Elixir]</A>
count = add_int("count")
for i in range(count):
    add_long("ItemUid")
    id = add_int("ItemId")
    add_int("Rarity")
    decode_item(id)
