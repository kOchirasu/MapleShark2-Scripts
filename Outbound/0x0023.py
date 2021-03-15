from script_api import *
from common import *

f = AddByte("Function")
if f == 0:
    AddInt("NpcId")
    AddByte("Unknown")
elif f == 3:
    AddByte("Index?")
    AddByte("UseVoucher") # sub_821610
    AddInt("Unknown")
    # Might not be hair here
    DecodeEquipColor()
    AddInt("AppearanceFlag")
    AddField("Back Hair Position", 4 * 7)
    AddField("Front Hair Position", 4 * 7)
elif f == 4:
    AddLong("Unknown")
elif f == 5: # change hair/eyes color
    AddByte("Index?") # Since it's hair color, no style here?
    AddByte("UseVoucher") # sub_821610
    AddLong("HairUid")
    DecodeEquipColor()
    AddInt("AppearanceFlag")
    AddField("Back Hair Position", 4 * 7)
    AddField("Front Hair Position", 4 * 7)
elif f == 6: # change skin color
    AddByte("Index?")
    DecodeSkinColor()
    AddByte("UseVoucher") # sub_821610
elif f == 7: # randomize hair
    AddInt("ShopId")
    AddBool("UseVoucher")
elif f == 10:
    AddShort("Type")
elif f == 12:
    AddByte("Unknown")
elif f == 16: # save hair
    AddLong("HairUid")
elif f == 18: # delete hair
    AddLong("SaveUid")
    AddBool("True")
elif f == 22: # gear dye
    count = AddByte("count")
    for i in range(count):
        with Node("Item " + str(i)):
            AddByte("Unknown") # 1
            AddField("Unknown", 15)
            AddLong("ItemUid")
            AddInt("ItemId")
            DecodeEquipColor()
            AddInt("AppearanceFlag")
elif f == 23:
    AddLong("Unknown")
