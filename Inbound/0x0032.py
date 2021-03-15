from script_api import *
from common import *

def DecodeCost():
    with Node("Cost?", True):
        AddByte("CurrencyType") # 0 = mesos, 9 = meret, 1 = custom?
        AddInt("CurrencyItemId") # if type == 1?
        AddInt("Amount")
        AddString("UnknownStr+52")


f = AddByte("Function")
if f == 0:
    AddByte("Unknown+9")
    AddInt("ShopId")
    AddInt("Unknown+14") # 1-Hair, 3-Face, 4-Skin, 5-Dye
    AddInt("VoucherItemId")
    AddByte("UseCustomCurrency")
    AddInt("CurrencyId")
    AddInt("ShopIndex???")
    AddByte("Unknown+31")
    DecodeCost()
    DecodeCost()
    AddByte("Unknown+54")
    AddByte("Unknown+55")
    count = AddShort("count")
    for i in range(count):
        with Node("Option " + str(i)):
            AddInt("CosmeticId")
            AddBool("IsNew")
            AddShort("Unknown+63") # 0
            AddInt("AchievmentId")
            AddByte("AchievementRank")
            DecodeCost()
elif f == 1:
    AddByte("Unknown+9")
    AddInt("ShopId")
    AddInt("Unknown+14")
    AddInt("VoucherItemId")
    AddByte("Unknown+22")
    AddInt("Unknown+23")
    AddInt("Unknown+27")
    AddByte("Unknown+31")
    DecodeCost()
    DecodeCost()
    AddByte("Unknown+54")
    AddByte("Unknown+55")
    AddUnicodeString("UnknownStr")
elif f == 2:
    AddByte("Unknown+9")
    AddInt("ShopId")
    AddInt("Unknown+14")
    AddInt("VoucherItemId")
    AddByte("Unknown+22")
    AddInt("Unknown+23")
    AddInt("Unknown+27")
    AddByte("Unknown+31")
    DecodeCost()
    DecodeCost()
    AddByte("Unknown+54")
    AddByte("Unknown+55")
    AddUnicodeString("UnknownStr")
elif f == 3:
    AddInt("Unknown")
elif f == 4:
    AddLong("Unknown")
elif f == 5:
    AddLong("Unknown")
    AddInt("Unknown")
elif f == 7:
    AddLong("Unknown")
    AddInt("Unknown")
elif f == 8:
    AddInt("Unknown+9")
elif f == 9: # useVoucher
    AddInt("ItemId")
    AddInt("Amount")
elif f == 14:
    AddShort("Unknown+9")
elif f == 15:
    count = AddShort("count")
    for i in range(count):
        with Node("Hair " + str(i)):
            id = AddInt("ItemId")
            AddLong("ItemUid")
            AddInt("Unknown+23")
            AddLong("CreationTime")
            DecodeEquipColor()
            AddInt("AppearanceFlag")
            AddField("Back Hair Position", 4 * 7)
            AddField("Front Hair Position", 4 * 7)
elif f == 16: # Saved Hair
    AddLong("HairUid")
    AddLong("SaveUid")
    AddByte("Index?")
    AddLong("Timesaved")
elif f == 18: # delete hair
    AddLong("SaveUid")
elif f == 20:
    AddByte("Unknown")
    AddShort("Unknown")
