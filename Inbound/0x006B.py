from script_api import *
from common import *

def decode_cube_item_info():
    with Node("CubeItemInfo"):
        add_int("ItemId")
        add_long("ItemUid")
        add_long("Unknown")
        b = add_bool("IsUgc")
        if b:
            decode_ugc_data()    


f = add_byte("function")
if f == 0:
    add_int("Unknown")
    add_int("Unknown")
    # ...
elif f == 1: # confirm hold cube
    add_int("UserObjectId")
    decode_cube_item_info()
elif f == 2:
    b = add_bool("Unknown")
    if not b:
        add_int("PlotId")
        add_int("Unknown")
        add_unicode_str("HomeName")
        add_long("PlotExpiration")
        add_long("OwnerAccountId")
    # GOTO:148
    # Client Send OP:0x37, FUNC:21
elif f == 4: # finish buying plot
    pass # none
elif f == 5: # forfeit plot
    b = add_bool("Unknown")
    if not b:
        add_int("PlotId")
        add_int("Unknown")
        add_bool("Unknown")
    # GOTO:148
elif f == 7: # complete forfeit plot
    add_short("MsgCode") # if 117, Err=1755, else: 1804
    add_bool("Unknown") # if true, 12540, else: 12468
    add_int("PlotMapId")
    add_int("PlotId")
elif f == 9: # Also 40, 41
    b = add_bool("Unknown")
    if not b:
        add_long("OwnerAccountId")
    # GOTO: 148
elif f == 10: # confirm place cube
    b = add_bool("UnknownB")
    add_int("UserObjectId")
    if b: # This is sent first, item is removed from warehouse
        add_int("UserObjectId")
    else: # Then this is sent to place the block
        add_int("UserObjectId")
        add_int("Unknown") # Amount?
        add_int("Unknown")
        add_int("CoordB")
        add_long("Uid")
        decode_cube_item_info()
        add_bool("UnknownB")
        add_float("Rotation")
        add_int("Unknown")
        b = add_bool("UnknownB")
        if b:
            add_unicode_str("UnknownStr")
            add_byte("Unknown")
elif f == 12: # Remove cube (clearing map)
    b = add_bool("UnknownB")
    add_int("UserObjectId")
    if b:
        add_int("Unknown")
    else:
        add_int("UserObjectId")
        add_float("CoordB") # COERCE_FLOAT
        add_bool("Unknown") # 0
elif f == 14: # rotate
    b = add_bool("UnknownB")
    add_int("UserObjectId")
    if b:
        add_int("Unknown")
    else:
        add_int("UserObjectId")
        add_int("CoordB")
        add_float("Rotation")
elif f == 15: # replace cube (also used for loading save map)
    b = add_bool("UnknownB")
    add_int("UserObjectId")
    if b:
        add_int("Unknown")
    else:
        add_int("UserObjectId")
        add_float("CoordB") # COERCE_FLOAT
        add_long("Uid")
        decode_cube_item_info()
        add_bool("UnknownB")
        add_float("Rotation")
        add_int("Unknown")
elif f == 17: # confirm liftup object
    b = add_bool("UnknownB")
    if b:
        pass # GOTO: 139
    else:
        add_float("UserObjectId") # COERCE_FLOAT
        add_int("CoordB")
        add_int("ItemId")
        add_int("ServerTick") # next spawn time
elif f == 18: # swing liftup object
    b = add_bool("UnknownB")
    add_int("UserObjectId")
    if b:
        pass # GOTO: 139
elif f == 20: # load home
    add_int("UserObjectId")
    add_int("MapId") # Private Residence (62000000)
    add_int("PlotMapId")
    add_int("PlotId")
    add_float("Unknown") # COERCE_FLOAT
    add_unicode_str("HouseName")
    add_long("Plot Expiration")
    add_long("LastUpdated")
    add_bool("UnknownB") # 1
    # Send RequestSetCraftMode (On some conditions)
elif f == 21: # Set plot name
    b = add_bool("UnknownB")
    if b:
        add_int("Unknown") # LABEL_138
    else:
        add_long("OwnerAccountId")
        add_int("PlotId")
        add_int("Unknown")
        add_unicode_str("HomeName")
elif f == 22: # Buy/extend/forfeit plot
    add_int("PlotId")
    add_int("Unknown")
    add_byte("Unknown") # 1
    add_long("ExpirationTime")
elif f == 24: # set password
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
elif f == 25: # confirm thumbs up (can't vote anymore)
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_long("VotingAccountId")
        add_long("TimeNow")
elif f == 26:
    pass # none
elif f == 27:
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
        add_float("Unknown") # COERCE_FLOAT
elif f == 28: # Broadcast after vote
    add_int("WeeklyArchitectScore")
    add_int("TotalArchitectScore")
elif f == 29: # set home message
    b = add_bool("Unknown")
    if b: # includes LABEL 138, 139, 141
        add_int("Unknown")
    else:
        add_unicode_str("Message")
elif f == 32:
    pass # none
elif f == 33:
    pass # none
elif f == 34:
    add_int("OutsideMapID")
elif f == 36:
    count = add_byte("count")
    add_int("Unknown")
    for i in range(count):
        add_byte("Unknown")
        add_long("Unknown")
    # Client Send OP:0x37, FUNC:48
elif f == 37: # confirm increase area
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Area")
elif f == 38: # confirm decrease area
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Area")
elif f == 39: # design rank reward
    add_long("AccountId")
    add_long("Timestamp")
    add_long("Interior Desgin Rank")
    add_long("Interior Design Score")
    count = add_int("count")
    for i in range(count):
        add_int("TitleRelated")
elif f == 42: # set permission #1
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 43: # set permission #2
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 44: # confirm increase height
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Height")
elif f == 45: # confirm decrease height
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Height")
elif f == 46: # confirm save house
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_long("SaveUid")
        add_int("Slot")
        add_unicode_str("SaveName") # No Title
        add_long("Timestamp")
elif f == 50:
    add_long("Unknown")
elif f == 51: # change background
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Index")
elif f == 52: # change lighting
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Index")
elif f == 53:
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
elif f == 54: # change camera
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Index")
elif f == 55:
    add_short("Unknown")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
        add_float("Unknown") # COERCE_FLOAT
elif f == 56:
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_long("Unknown")
        add_long("Unknown")
elif f == 57:
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_long("Unknown")
elif f == 58:
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_long("Unknown")
elif f == 59:
    count = add_int("count")
    for i in range(count):
        add_long("Unknown")
elif f == 60:
    add_long("Unknown")
    add_long("Unknown")
elif f == 61:
    n = add_byte("Unknown")
    if n == 100:
        add_byte("Unknown")
elif f == 62:
    b = add_bool("Unknown")
    if b:
        pass # GOTO: 148
    else:
        add_byte("Unknown")
        add_byte("Unknown")
elif f == 63:
    add_byte("Unknown")
    add_long("Unknown")
    # DecodeUgcRelated2
elif f == 64:
    b = add_bool("Unknown")
    if b:
        pass # LABEL: 148
    else:
        add_long("SaveUid")
        add_int("Slot")
        add_unicode_str("SaveName")
        add_long("Timestamp")
elif f == 67:
    count = add_byte("count")
    add_int("Unknown")
    for i in range(count):
        add_byte("Unknown")
        add_long("Unknown")
    b = add_bool("Unknown")
    # if !b
    # Client Send OP:0x37, FUNC:70
elif f == 69:
    add_long("Unknown")
elif f == 71:
    n = add_int("Unknown")
    if n == 1 or n == 2:
        pass # do something
    elif n == 3:
        pass # do something
    elif n == 4:
        pass # do something
