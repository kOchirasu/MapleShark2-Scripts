from script_api import *
from common import *

def DecodeCubeItemInfo():
    with Node("CubeItemInfo"):
        AddInt("ItemId")
        AddLong("ItemUid")
        AddLong("Unknown")
        b = AddBool("IsUgc")
        if b:
            DecodeUgcData()
    

# BROADCASTED
AddInt("PlayerObjectId")
b = AddBool("IsStart")
if b:
    DecodeCubeItemInfo()
    AddInt("Unknown")
