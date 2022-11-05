''' TRADE '''
from script_api import *
from item import *

f = add_byte("function")
if f == 0: # Receive trade request
    add_unicode_str("PlayerName")
    add_long("CharacterId")
elif f == 1: # error
    message = add_byte("message")
    add_unicode_str("name") # used for 0,1,2,3,5,6,12,15,16
    add_int("itemId?") # used for error 20,21
    add_int("level") # used for error 20,21
    '''
    if message == 0:
        pass # s_trade_error_system
    elif message == 1:
        pass # s_trade_error_distance
    elif message == 2:
        pass # s_trade_error_already_request
    elif message == 3:
        pass # s_trade_error_trading_now
    elif message == 5:
        pass # s_trade_error_latched
    elif message == 6:
        pass # s_trade_error_decline
    elif message == 7:
        pass # s_trade_error_itemcount
    elif message == 8:
        pass # s_trade_error_slotcount
    elif message == 9:
        pass # s_trade_error_itemnone
    elif message == 10:
        pass # s_trade_error_pvp
    elif message == 11:
        pass # s_trade_error_mapLimit
    elif message == 12:
        pass # s_trade_error_timeout
    elif message == 13:
        pass # s_trade_error_invalid_meso
    elif message == 14:
        pass # s_trade_error_meso
    elif message == 15:
        pass # s_trade_error_target_property_protection_time
    elif message == 16:
        pass # s_trade_error_target_fatigue_penalty
    elif message == 17:
        pass # send 0x0D, and sub_E30870(0, 0)
    elif message == 18:
        pass # s_trade_error_restricted_userlevel_max
    elif message == 19:
        pass # s_trade_error_restricted_target_userlevel_max
    elif message == 20:
        pass # s_trade_error_send_restricted_by_user_level_ex
    elif message == 21:
        pass # s_trade_error_recv_restricted_by_user_level_ex
    else:
        pass # s_trade_error, send 0x0D
    '''
elif f == 2: # confirm request trade
    pass # none
elif f == 4: # trade declined
    add_unicode_str("PlayerName")
elif f == 5: # begin trade
    add_long("CharacterId")
elif f == 6: # end trade
    add_bool("Success")
elif f == 8: # Add item
    add_byte("Index") # (0 = left, 1 = right)
    id = add_int("ItemId")
    add_long("ItemUid")
    add_int("Rarity")
    add_int("TradeSlot")
    add_int("Amount")
    add_int("TradeSlot")
    decode_item(id)
elif f == 9: # RemoveItem
    add_byte("Index") # (0 = left, 1 = right)
    add_int("TradeSlot")
    add_long("ItemUid")
elif f == 10: # set money
    add_byte("Index")
    add_long("Mesos")
elif f == 11: # finalize trade
    add_byte("Index") # (0 = left, 1 = right)
elif f == 12:
    t = add_byte("Index")
    if t == 1:
        pass # s_trade_unlatch_me: The other player altered their offer.
    else:
        pass # s_trade_unlatch_oppnent: The other player is considering your new offer.
elif f == 13: # finalize confirm trade
    add_byte("Index") # (0 = left, 1 = right)
elif f == 14:
    pass # s_trade_already_requested
