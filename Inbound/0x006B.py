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


f = AddByte("function")
if f == 0:
    AddInt("Unknown")
    AddInt("Unknown")
    # ...
elif f == 1: # confirm hold cube
    AddInt("UserObjectId")
    DecodeCubeItemInfo()
elif f == 2:
    b = AddBool("Unknown")
    if not b:
        AddInt("PlotId")
        AddInt("Unknown")
        AddUnicodeString("HomeName")
        AddLong("PlotExpiration")
        AddLong("OwnerAccountId")
    # GOTO:148
    # Client Send OP:0x37, FUNC:21
elif f == 4: # finish buying plot
    pass # none
elif f == 5: # forfeit plot
    b = AddBool("Unknown")
    if not b:
        AddInt("PlotId")
        AddInt("Unknown")
        AddBool("Unknown")
    # GOTO:148
elif f == 7: # complete forfeit plot
    AddShort("MsgCode") # if 117, Err=1755, else: 1804
    AddBool("Unknown") # if true, 12540, else: 12468
    AddInt("PlotMapId")
    AddInt("PlotId")
elif f == 9: # Also 40, 41
    b = AddBool("Unknown")
    if not b:
        AddLong("OwnerAccountId")
    # GOTO: 148
elif f == 10: # confirm place cube
    b = AddBool("UnknownB")
    AddInt("UserObjectId")
    if b: # This is sent first, item is removed from warehouse
        AddInt("UserObjectId")
    else: # Then this is sent to place the block
        AddInt("UserObjectId")
        AddInt("Unknown") # Amount?
        AddInt("Unknown")
        AddInt("CoordB")
        AddLong("Uid")
        DecodeCubeItemInfo()
        AddBool("UnknownB")
        AddFloat("Rotation")
        AddInt("Unknown")
        b = AddBool("UnknownB")
        if b:
            AddUnicodeString("UnknownStr")
            AddByte("Unknown")
elif f == 12: # Remove cube (clearing map)
    b = AddBool("UnknownB")
    AddInt("UserObjectId")
    if b:
        AddInt("Unknown")
    else:
        AddInt("UserObjectId")
        AddFloat("CoordB") # COERCE_FLOAT
        AddBool("Unknown") # 0
elif f == 14: # rotate
    b = AddBool("UnknownB")
    AddInt("UserObjectId")
    if b:
        AddInt("Unknown")
    else:
        AddInt("UserObjectId")
        AddInt("CoordB")
        AddFloat("Rotation")
elif f == 15: # replace cube (also used for loading save map)
    b = AddBool("UnknownB")
    AddInt("UserObjectId")
    if b:
        AddInt("Unknown")
    else:
        AddInt("UserObjectId")
        AddFloat("CoordB") # COERCE_FLOAT
        AddLong("Uid")
        DecodeCubeItemInfo()
        AddBool("UnknownB")
        AddFloat("Rotation")
        AddInt("Unknown")
elif f == 17: # confirm liftup object
    b = AddBool("UnknownB")
    if b:
        pass # GOTO: 139
    else:
        AddFloat("UserObjectId") # COERCE_FLOAT
        AddInt("CoordB")
        AddInt("ItemId")
        AddInt("ServerTick") # next spawn time
elif f == 18: # swing liftup object
    b = AddBool("UnknownB")
    AddInt("UserObjectId")
    if b:
        pass # GOTO: 139
elif f == 20: # load home
    AddInt("UserObjectId")
    AddInt("MapId") # Private Residence (62000000)
    AddInt("PlotMapId")
    AddInt("PlotId")
    AddFloat("Unknown") # COERCE_FLOAT
    AddUnicodeString("HouseName")
    AddLong("Plot Expiration")
    AddLong("LastUpdated")
    AddBool("UnknownB") # 1
    # Send RequestSetCraftMode (On some conditions)
elif f == 21: # Set plot name
    b = AddBool("UnknownB")
    if b:
        AddInt("Unknown") # LABEL_138
    else:
        AddLong("OwnerAccountId")
        AddInt("PlotId")
        AddInt("Unknown")
        AddUnicodeString("HomeName")
elif f == 22: # Buy/extend/forfeit plot
    AddInt("PlotId")
    AddInt("Unknown")
    AddByte("Unknown") # 1
    AddLong("ExpirationTime")
elif f == 24: # set password
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
elif f == 25: # confirm thumbs up (can't vote anymore)
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddLong("VotingAccountId")
        AddLong("TimeNow")
elif f == 26:
    pass # none
elif f == 27:
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
        AddFloat("Unknown") # COERCE_FLOAT
elif f == 28: # Broadcast after vote
    AddInt("WeeklyArchitectScore")
    AddInt("TotalArchitectScore")
elif f == 29: # set home message
    b = AddBool("Unknown")
    if b: # includes LABEL 138, 139, 141
        AddInt("Unknown")
    else:
        AddUnicodeString("Message")
elif f == 32:
    pass # none
elif f == 33:
    pass # none
elif f == 34:
    AddInt("OutsideMapID")
elif f == 36:
    count = AddByte("count")
    AddInt("Unknown")
    for i in range(count):
        AddByte("Unknown")
        AddLong("Unknown")
    # Client Send OP:0x37, FUNC:48
elif f == 37: # confirm increase area
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Area")
elif f == 38: # confirm decrease area
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Area")
elif f == 39: # design rank reward
    AddLong("AccountId")
    AddLong("Timestamp")
    AddLong("Interior Desgin Rank")
    AddLong("Interior Design Score")
    count = AddInt("count")
    for i in range(count):
        AddInt("TitleRelated")
elif f == 42: # set permission #1
    AddByte("PermissionType")
    AddByte("PermissionSetting")
elif f == 43: # set permission #2
    AddByte("PermissionType")
    AddByte("PermissionSetting")
elif f == 44: # confirm increase height
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Height")
elif f == 45: # confirm decrease height
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Height")
elif f == 46: # confirm save house
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddLong("SaveUid")
        AddInt("Slot")
        AddUnicodeString("SaveName") # No Title
        AddLong("Timestamp")
elif f == 50:
    AddLong("Unknown")
elif f == 51: # change background
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Index")
elif f == 52: # change lighting
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Index")
elif f == 53:
    AddLong("Unknown")
    AddLong("Unknown")
    AddLong("Unknown")
    AddLong("Unknown")
elif f == 54: # change camera
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Index")
elif f == 55:
    AddShort("Unknown")
    count = AddInt("count")
    for i in range(count):
        AddInt("Unknown")
        AddFloat("Unknown") # COERCE_FLOAT
elif f == 56:
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddLong("Unknown")
        AddLong("Unknown")
elif f == 57:
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddLong("Unknown")
elif f == 58:
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddLong("Unknown")
elif f == 59:
    count = AddInt("count")
    for i in range(count):
        AddLong("Unknown")
elif f == 60:
    AddLong("Unknown")
    AddLong("Unknown")
elif f == 61:
    n = AddByte("Unknown")
    if n == 100:
        AddByte("Unknown")
elif f == 62:
    b = AddBool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        AddByte("Unknown")
        AddByte("Unknown")
elif f == 63:
    AddByte("Unknown")
    AddLong("Unknown")
    # DecodeUgcRelated2
elif f == 64:
    b = AddBool("Unknown")
    if b:
        pass # LABEL: 148
    else:
        AddLong("SaveUid")
        AddInt("Slot")
        AddUnicodeString("SaveName")
        AddLong("Timestamp")
elif f == 67:
    count = AddByte("count")
    AddInt("Unknown")
    for i in range(count):
        AddByte("Unknown")
        AddLong("Unknown")
    b = AddBool("Unknown")
    # if !b
    # Client Send OP:0x37, FUNC:70
elif f == 69:
    AddLong("Unknown")
elif f == 71:
    n = AddInt("Unknown")
    if n == 1 or n == 2:
        pass # do something
    elif n == 3:
        pass # do something
    elif n == 4:
        pass # do something
