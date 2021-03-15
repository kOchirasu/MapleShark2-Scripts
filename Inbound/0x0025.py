from script_api import *
from common import *

AddInt("UserObjectId")
id = AddInt("ItemId")
AddLong("ItemUid")
AddUnicodeString("EquipSlot")
AddInt("Rarity?")
AddByte("Unknown")
DecodeItem(id)
