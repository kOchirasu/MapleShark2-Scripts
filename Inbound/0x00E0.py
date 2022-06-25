''' ITEM SOCKET '''
from script_api import *
from item import *

f = add_byte("function")

# ItemSocketSystemPageSocketTransfer
if f == 13:
    add_long("ItemUid")
    decode_gem_sockets()
    add_long("ItemUid")
    decode_gem_sockets()
    b = add_bool("Transfer")
    if b:
        decode_item_transfer()
elif f == 16:
    pass
# ItemSocketSystemPageGemStoneManage
elif f == 9: # EquipGemstone
    add_long("EquipUid")
    #add_long("GemstoneUid") # This uid here becomes changed from actual gem uid
    add_byte("SocketSlot")
    b = add_bool("flag")
    if b:
        decode_gemstone()
elif f == 11: # UnequipGemstone
    add_long("EquipUid")
    add_byte("SocketSlot")
# ItemSocketSystemPageGemStoneUpgrade
elif f == 5: # UpgradeGemstone
    add_long("ItemUid")
    add_byte("Slot")
    add_bool("Amount?") # 1
    add_byte("rarity") # 4
    add_long("GemstoneUid")
    b = add_bool("Success")
    if b:
        decode_gemstone()
elif f == 7: # StageUpgradeGemstone
    add_long("EquipUid") # If gemstone is on an equip, else: 0
    add_byte("Equipped") # 255 = not equipped, 1 = equipped?
    add_long("GemstoneUid")
    add_float("SuccessRate")
elif f == 16:
    pass # ItemSocketSystemPageBase::SaleParam
# ItemSocketSystemPageSocketUnlock
elif f == 1: # UnlockSocket
    b = add_bool("Success")
    add_long("ItemUid")
    if b:
        add_byte("Slot")
        decode_gem_sockets()
        b = add_bool("Transfer")
        if b:
            decode_item_transfer()
elif f == 3: # StageUnlockSocket
    add_long("EquipUid")
    add_byte("Slot") # FF
    add_long("MaterialUid")
    add_float("SuccessRate")
elif f == 16:
    pass # ItemSocketSystemPageBase::SaleParam
# CommonErrorHandler
elif f == 18:
    add_byte("code") # used as args
    message = add_int("message")
    if message == 1:
        pass # s_itemsocketsystem_error_invalid_target
    elif message == 2:
        pass # s_itemsocketsystem_error_invalid_target_gemstone
    elif message == 3:
        pass # s_itemsocketsystem_error_invalid_target_ingredient
    elif message == 4:
        pass # s_itemsocketsystem_error_invalid_target_ingredient_count
    elif message >= 5 and message <= 12:
        pass # s_itemsocketsystem_error_server_default_msgbox
    elif message == 15:
        pass # s_itemsocketsystem_error_socket_lock
    elif message == 16:
        pass # s_itemsocketsystem_error_socket_used
    elif message == 17:
        pass # s_itemsocketsystem_error_socket_empty
    elif message == 18:
        pass # s_itemsocketsystem_error_socket_unlock_all
    elif message == 20:
        pass # s_itemsocketsystem_error_gemstone_maxlevel
    elif message == 21:
        pass # s_itemsocketsystem_error_lack_price
    elif message == 22:
        pass # None
    elif message == 23:
        pass # s_itemsocketsystem_error_bind_owner
    else:
        pass # s_itemsocketsystem_error_server_default
