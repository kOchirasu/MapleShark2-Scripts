''' WEDDING '''
from script_api import *
from wedding import *

def decode_wedding_proxy(): # WeddingProxy?
    add_long("unknown")
    add_byte("unknown")
    add_long("unknown")
    add_long("unknown")
    sub_6839D0()
    sub_6839D0()
    add_long("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
    sub_684B00()

def sub_6839D0():
    add_long("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
    add_bool("unknown")

def sub_684B00():
    count = add_int("count")
    for i in range(count):
        add_short("unknown")
        add_long("unknown")
        add_long("unknown")

def decode_wedding_guest(): # WeddingGuest
    add_long("unknown")
    add_long("GuestUid")
    add_unicode_str("unknown")


f = add_byte("function")
if f == 0:
    decode_wedding_proxy()
elif f == 1:
    decode_wedding_hall_ticket()
    count = add_int("count")
    for i in range(count):
        add_long("unknown")
        add_long("unknown")
elif f == 2:
    message = add_byte("message")
    '''
    if message < 18:
        if message == 2:
            pass # s_wedding_result_decline_propose
        elif message == 3:
            # s_wedding_msg_box_propose_to
            # s_msg_popup_time
            # SendPacket 0xBC function 5
            pass
        elif message == 4:
            pass # s_wedding_result_cancel_propose_to
        elif message == 5:
            pass # s_wedding_result_cancel_propose_from
        elif message == 6:
            pass # s_wedding_result_cancel_propose_expire
        elif message == 15:
            pass # s_wedding_result_send_wedding_hall_reservation
        elif message == 16:
            pass # s_wedding_result_send_wedding_hall_reservation_change
        elif message == 17:
            pass # s_wedding_result_send_wedding_hall_reservation_cancel

        if message == 1 or message == 2 or message == 5 or message == 6:
            pass # StateWeddingEmotionData
    else:
        wedding_error(message)
    '''
elif f == 3:
    add_long("unknown")
    # s_wedding_msg_box_propose_from
    # s_msg_popup_time
    # SendPacket 0xBC function 4
elif f == 6: # s_wedding_propose_ok
    decode_wedding_proxy()
elif f == 8: # s_wedding_divorce_mutual_msgbox
    pass
    # SendPacket 0xBC function 9
elif f == 13: # s_wedding_reservation_request_messagebox
    decode_wedding_hall_ticket()
elif f == 15: # s_wedding_hall_reserve_ok
    decode_wedding_hall_ticket()
elif f == 16: # s_wedding_hall_reservation_cancel_request
    pass
    # SendPacket 0xBC function 18
elif f == 17:
    n = add_short("unknown")
    if n == 10:
        pass # s_wedding_hall_reservation_cancel_no_refund_decline
    elif n == 34:
        pass # s_wedding_hall_reservation_cancel_no_refund_not_find_partner
    # SendPacket 0xBC function 17
elif f == 19:
    pass # s_wedding_hall_reserve_cancel_ok
elif f == 20:
    decode_wedding_hall_ticket()
    add_long("unknown")
    # some condition:
    # s_common_merat, s_wedding_reservation_change_request_messagebox
    # SendPacket 0xBC function 21
elif f == 22: # s_wedding_hall_reserve_change_ok
    decode_wedding_hall_ticket()
    add_long("unknown")
elif f == 23:
    pass # delete WeddingHallTicket
elif f == 24:
    # this function first checks that player mapId is 62000000 (Home)
    add_long("unknown")
    decode_wedding_hall_ticket()
    pass
elif f == 25: # UIWeddingHallListDialog
    add_long("unknown")
elif f == 27:  # UIWeddingGuestDialog
    decode_wedding_guest()
    # s_wedding_result_err_not_find_character
elif f == 29: # UIWeddingInvitationDialog
    pass # s_wedding_invitation_ok
elif f == 30:
    t = add_byte("type")
    if t == 1:
        pass # s_wedding_mutual_agree_start_acting
    elif t == 2:
        pass # s_wedding_mutual_agree_end_acting
    elif t == 3:
        add_unicode_str("unknown")
        # s_wedding_enter_nickname, s_wedding_enter_nickname_confirm_checkbox
    # SendPacket 0xBC function 30
elif f == 31:
    add_byte("unknown") # checks if this is 3
elif f == 35: # UIWeddingDialog
    pass # setProfile
elif f == 39:
    t = add_byte("type") # StateWeddingEmotionData
    # checks player state == {1, 2, 71}
    if t == 1:
        pass # Emotion_HandKiss_A
    elif t == 2:
        add_int("unknown")
        add_bool("unknown")
        add_bool("unknown")
        add_int("unknown")
