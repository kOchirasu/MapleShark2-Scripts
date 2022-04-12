''' shared WEDDING structs '''
from script_api import *

def wedding_error(message):
    if message == 19:
        pass # s_wedding_result_err_wedding_block_age_to
    elif message == 20:
        pass # s_wedding_result_err_wedding_block_age_from
    elif message == 21:
        pass # s_wedding_result_err_wedding_block_gender
    elif message == 22:
        pass # s_wedding_result_err_not_buddy
    elif message == 23:
        pass # s_wedding_result_err_propose_state_to
    elif message == 24:
        pass # s_wedding_result_err_marriage_state_to
    elif message == 25:
        pass # s_wedding_result_err_coolingoff_state_to
    elif message == 26:
        pass # s_wedding_result_err_prpose_cooltime_state_to
    elif message == 27:
        pass # s_wedding_result_err_propose_state_from
    elif message == 28:
        pass # s_wedding_result_err_mareriage_state_from
    elif message == 29:
        pass # s_wedding_result_err_coolingoff_state_from
    elif message == 30:
        pass # s_wedding_result_err_propose_cooltime_state_from
    elif message == 31:
        pass # s_wedding_result_err_not_find_propose_item
    elif message == 32:
        pass # s_wedding_result_err_propose_distance
    elif message == 33:
        pass # s_wedding_result_err_already_propose_request
    elif message == 34:
        pass # s_wedding_result_err_same_field
    elif message == 35:
        pass # s_wedding_result_err_only_promise_user
    elif message == 36:
        pass # s_wedding_result_err_invalid_wedding_hall
    elif message == 37:
        pass # s_wedding_result_err_lack_merat
    elif message == 38:
        pass # s_wedding_result_err_maintenance_time
    elif message == 39:
        pass # s_wedding_result_not_find_weddinghall
    elif message == 40:
        pass # s_wedding_result_already_send_invitation
    elif message == 41:
        pass # s_wedding_result_late_promise_time
    elif message == 42:
        pass # s_wedding_result_late_wedding_reserve_modify
    elif message == 43:
        pass # s_wedding_result_already_reservation
    elif message == 44:
        pass # s_wedding_result_already_same_reservation
    elif message == 45:
        pass # s_wedding_result_invaild_state_divorce
    elif message == 46:
        pass # s_wedding_result_lack_marriage_date
    elif message == 47:
        pass # s_wedding_result_lack_meso_divorce
    elif message == 48:
        pass # s_wedding_result_late_divorce_agree
    elif message == 49:
        pass # s_wedding_result_invalid_divorce_agree_user
    elif message == 50:
        pass # s_wedding_result_only_marriage_user
    elif message == 51:
        pass # s_wedding_result_wedding_invitation_count
    elif message == 52:
        pass # s_wedding_result_lack_meso_invitation
    elif message == 53:
        pass # s_wedding_result_early_remind_wedding
    elif message == 54:
        pass # s_wedding_result_early_wedding_reserve
    elif message == 55:
        pass # s_wedding_result_divorcecancel
    elif message == 56:
        pass # s_wedding_visit_failed_common
    elif message == 57:
        pass # s_wedding_visit_failed_disablemap
    elif message == 58:
        pass # s_wedding_visit_failed_dead
    elif message == 59:
        pass # s_wedding_visit_failed_same_place
    elif message == 60:
        pass # s_wedding_visit_failed_solo_instance
    elif message == 61:
        pass # s_wedding_visit_failed_invalid_time
    elif message == 62:
        pass # s_wedding_result_only_booking_character
    elif message == 63:
        pass # s_wedding_result_already_weddinghall_reserve
    elif message == 64:
        pass # s_wedding_result_lack_coupon
    else:
        pass # s_wedding_result_err_system

def decode_wedding_hall_reservation_fee(): # WeddingHallReservationFee
    for i in range(4):
        add_long("unknown")
    add_long("unknown")

def decode_wedding_hall_ticket(): # WeddingHallTicket
    add_long("unknown")
    add_int("unknown")
    add_int("unknown")
    add_long("unknown")
    add_bool("unknown")
    add_long("unknown")
    add_long("unknown")
    add_unicode_str("unknown")
    add_unicode_str("unknown")
    decode_wedding_hall_reservation_fee()
    add_int("unknown")
