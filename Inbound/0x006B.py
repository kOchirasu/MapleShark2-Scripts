''' RESPONSE_CUBE '''
from script_api import *
from common import *

def error_handler(code): # sub_9EF4B0
    if code == 34:
        pass # s_err_lack_merat_ask. s_cannot_charge_merat if MeratMarketClosing|Feature_296
    elif code != 1:
        pass # sub_9EE0E0 and sub_9EE280 (lots of string mappings...)


f = add_byte("function")
if f == 0:
    add_int("PlayerObjectId")
    add_int("Unknown")
elif f == 1: # confirm hold cube
    add_int("PlayerObjectId")
    decode_cube_item_info()
elif f == 2:
    result = add_bool("result")
    if result == 0:
        add_int("PlotId")
        add_int("Unknown")
        add_unicode_str("HomeName")
        add_long("PlotExpiration")
        add_long("OwnerAccountId")
    error_handler(result)
    # Client Send OP:0x37, FUNC:21
elif f == 4: # finish buying plot
    pass # s_ugcmap_buy_realestate
elif f == 5: # forfeit plot
    result = add_bool("result")
    if result == 0:
        add_int("PlotId")
        add_int("Unknown")
        add_bool("Unknown")
    error_handler(result)
elif f == 7: # complete forfeit plot
    mode = add_short("mode")
    if mode == 117:
        pass # s_ugcmap_already_expired
    else:
        pass # s_ugcmap_sell_realestate
    add_bool("UseMerat") # true ? returnHomeSkillMerat : returnHomeSkill
    add_int("PlotMapId")
    add_int("PlotId")
elif f == 9 or f == 24 or f == 40 or f == 41: # set password?
    result = add_bool("result")
    if result == 0:
        add_long("OwnerAccountId")
    error_handler(result)
elif f == 10: # confirm place cube
    error = add_bool("error")
    add_int("UserObjectId")
    if error: # This is sent first, item is removed from warehouse
        add_int("UserObjectId")
        # s_ugcmap_lift_error_msg
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
    error = add_bool("error")
    add_int("UserObjectId")
    if error:
        add_int("UserObjectId")
        # s_ugcmap_lift_error_msg
    else:
        add_int("UserObjectId")
        add_int("CoordB")
        add_bool("Unknown") # 0
elif f == 14: # rotate
    error = add_bool("error")
    add_int("UserObjectId")
    if error:
        add_int("UserObjectId")
        # s_ugcmap_lift_error_msg
    else:
        add_int("UserObjectId")
        add_int("CoordB")
        add_float("Rotation")
elif f == 15: # replace cube (also used for loading save map)
    error = add_bool("error")
    add_int("UserObjectId")
    if error:
        add_int("UserObjectId")
        # s_ugcmap_lift_error_msg
    else:
        add_int("UserObjectId")
        add_int("CoordB")
        add_long("Uid")
        decode_cube_item_info()
        add_bool("UnknownB")
        add_float("Rotation")
        add_int("Unknown")
elif f == 17: # confirm liftup object
    error = add_bool("error")
    add_int("UserObjectId")
    if error:
        pass # GOTO: 139
    else:
        add_int("CoordB")
        add_int("ItemId")
        add_int("ServerTick") # next spawn time
elif f == 18: # swing liftup object
    error = add_bool("error")
    add_int("UserObjectId")
    if error:
        pass # GOTO: 139
elif f == 20: # load home
    add_int("UserObjectId")
    add_int("MapId") # Private Residence (62000000)
    add_int("PlotMapId")
    add_int("PlotId")
    add_int("Unknown")
    add_unicode_str("HouseName")
    add_long("Plot Expiration")
    add_long("LastUpdated")
    add_bool("UnknownB") # 1
    # Send RequestSetCraftMode (On some conditions)
elif f == 21: # Set plot name
    result = add_bool("result")
    if result:
        add_int("UserObjectId") # LABEL_138
    else:
        add_long("OwnerAccountId")
        add_int("PlotId")
        add_int("Unknown")
        add_unicode_str("HomeName")
elif f == 22: # Buy/extend/forfeit plot
    # SaleStateData
    add_int("PlotId")
    add_int("Unknown")
    add_byte("state") # 1
    add_long("ExpirationTime")
elif f == 25: # confirm thumbs up (can't vote anymore)
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_long("VotingAccountId")
        add_long("TimeNow")
        # s_home_commend_success
elif f == 26: # userOutNotice
    pass # s_home_password_user_out_chat_msg, s_home_password_user_out_button
elif f == 27:
    count = add_int("count")
    for i in range(count):
        add_int("ServerTicks") # next spawn time?
        add_int("CoordB")
elif f == 28: # Broadcast after vote
    add_int("WeeklyArchitectScore")
    add_int("TotalArchitectScore")
elif f == 29: # set home message
    result = add_bool("result")
    if result: # includes LABEL 138, 139, 141
        add_int("UserObjectId")
    else:
        add_unicode_str("Message")
        # UIHomeInfoDialog
elif f == 32:
    pass # MyPc+264C = 1
elif f == 33:
    pass # MyPc+264C = 0
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
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Area")
        # s_ugcmap_area_level_extended_successfully
elif f == 38: # confirm decrease area
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Area")
        # s_ugcmap_area_level_shrink_successfully
elif f == 39: # design rank reward
    add_long("AccountId")
    add_long("Timestamp")
    add_long("Interior Desgin Rank")
    add_long("Interior Design Score")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown") # dword_1BF80D0
elif f == 42: # set permission #1
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 43: # set permission #2
    add_byte("PermissionType")
    add_byte("PermissionSetting")
elif f == 44: # confirm increase height
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Height")
        # s_ugcmap_height_level_extended_successfully
elif f == 45: # confirm decrease height
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Height")
        # s_ugcmap_height_level_shrink_successfully
elif f == 46: # confirm save house
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_long("SaveUid")
        add_int("Slot")
        add_unicode_str("SaveName") # No Title
        add_long("Timestamp")
elif f == 50: # UIUGCCubePaletteDialog
    add_long("WarehouseItemUid")
elif f == 51: # change background
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Index")
elif f == 52: # change lighting
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Index")
elif f == 53: # related to 56
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
    add_long("Unknown")
elif f == 54: # change camera
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Index")
elif f == 55:
    add_short("Unknown")
    count = add_int("count")
    for i in range(count):
        add_int("Unknown")
        add_int("Unknown")
elif f == 56: # related to 53
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_long("Unknown")
        add_long("Unknown")
elif f == 57: # related to 59
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_long("Unknown")
elif f == 58:
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_long("Unknown")
elif f == 59: # related to 57
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
    result = add_bool("result")
    if result:
        error_handler(result)
    else:
        add_byte("Unknown")
        add_byte("Unknown")
elif f == 63: # BlueprintItemData
    add_byte("Unknown")
    add_long("ItemUid")
    decode_blueprint()
elif f == 64:
    result = add_bool("result")
    if result:
        error_handler(result)
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
    result = add_bool("result")
    # if not result:
    # Client Send OP:0x37, FUNC:70
elif f == 69: # CubeMapInformationService
    add_long("Unknown")
elif f == 71:
    n = add_int("Unknown")
    if n == 1 or n == 2:
        pass # s_function_cube_error_invalid_cube
    elif n == 3:
        pass # s_function_cube_error_invalid_pos
    elif n == 4:
        pass # s_function_cube_error_invalid_summon_user
