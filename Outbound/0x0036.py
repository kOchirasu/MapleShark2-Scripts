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
    

AddByte("function") # this is also 0/1 but it's redundant
b = AddBool("IsStart")
if b:
    DecodeCubeItemInfo()
