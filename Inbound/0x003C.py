''' CURRENCY_TOKEN '''
from script_api import *

type = add_byte("type")
add_long("amount")
deduct = add_long("deduct")
overflow = add_long("overflow")

'''
if type == 3: # ValorToken
    if deduct > 0:
        pass # s_msg_take_honor_token
elif type == 4: # Treva
    if deduct > 0:
        pass # s_msg_take_karma_token
elif type == 5: # Rue
    if deduct > 0:
        pass # s_msg_take_lu_token
elif type == 6: # HaviFruit
    if deduct > 0:
        pass # s_msg_take_habi_token
elif type == 9: # ReverseCoin
    if deduct > 0:
        pass # s_msg_take_reverse_coin
elif type == 10: # MentorToken
    if deduct > 0:
        pass # s_msg_take_mentor_token
elif type == 11: # MenteeToken
    if deduct > 0:
        pass # s_msg_take_mentee_token
elif type == 12: # StarPoint
    if deduct > 0:
        pass # s_msg_take_star_point
elif type == 13: # MesoToken
    if deduct > 0:
        pass # s_msg_take_meso_market_token

if overflow > 0:
    pass # s_notify_currency_overflow
'''
