''' RESPONSE_RIDE '''
from script_api import *
from item import *

f = add_byte("Function")
if f == 0: # start riding
    add_int("PlayerObjectId")
    # DecodeRide
    mountType = add_byte("type")
    if mountType == 0: # RideOnAction
        add_int("MountId")
        add_int("MountObjectId")
    elif mountType == 1: # RideOnActionUseItem
        add_int("MountId") # 4, 5, 7, 4
        add_int("MountObjectId")
        add_int("MountId")
        add_long("MountUid")
        # UGC Packet data
        decode_ugc_item_look()
    elif mountType == 2: # RideOnActionAdditionalEffect
        add_int("MountId")
        add_int("MountObjectId")
        add_int("Id")
        add_short("Level")
    elif mountType == 3: # RideOnActionHideAndSeek
        add_int("MountId")
        add_int("MountObjectId")
elif f == 1: # stop riding
    add_int("PlayerObjectId")
    action = add_byte("action")
    if action == 0:
        add_byte("RideOffAction+16")
        pass # RideOffAction
    elif action == 1:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        add_byte("RideOffAction+32")
        add_int("RideOffAction+36")
        pass # RideOffActionUseSkill
    elif action == 2:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        add_unicode_str("unknown")
        pass # RideOffActionInteract
    elif action == 3:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        pass # RideOffActionTaxi
    elif action == 4:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        add_byte("RideOffAction+32")
        add_long("RideOffAction+20")
        pass # RideOffActionCashCall
    elif action == 5:
        add_byte("RideOffAction+16")
        pass # RideOffActionBeautyShop
    elif action == 6:
        add_byte("RideOffAction+16")
        add_byte("RideOffAction+28")
        add_int("RideOffAction+32")
        pass # RideOffActionTakeLR
    elif action == 7:
        add_byte("RideOffAction+16")
        pass # RideOffActionHold
    elif action == 8:
        add_byte("RideOffAction+16")
        add_long("RideOffAction+16")
        pass # RideOffActionRecall
    elif action == 9:
        add_byte("RideOffAction+16")
        add_long("RideOffAction+16")
        add_byte("RideOffAction+40")
        pass # RideOffActionSummonPetOn
    elif action == 10:
        add_byte("RideOffAction+16")
        add_long("RideOffAction+16")
        pass # RideOffActionSummonPetTransfer
    elif action == 11:
        add_byte("RideOffAction+16")
        add_byte("RideOffAction+28")
        pass # RideOffActionHomeConvenient
    elif action == 12:
        add_byte("RideOffAction+16")
        pass # RideOffActionDisableField
    elif action == 13:
        add_byte("RideOffAction+16")
        pass # RideOffActionDead
    elif action == 14:
        add_byte("RideOffAction+16")
        pass # RideOffActionAdditionalEffect
    elif action == 15:
        add_byte("RideOffAction+16")
        pass # RideOffActionRidingUI
    elif action == 16:
        add_byte("RideOffAction+16")
        add_unicode_str("unknown")
        add_int("RideOffAction+32")
        add_short("RideOffAction+36")
        add_int("RideOffAction+40")
        pass # RideOffActionHomemade
    elif action == 17:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        add_byte("RideOffAction+32")
        add_short("RideOffAction+36")
        pass # RideOffActionAutoInteraction
    elif action == 18:
        add_byte("RideOffAction+16")
        pass # RideOffActionAutoClimb
    elif action == 19:
        add_byte("RideOffAction+16")
        add_int("RideOffAction+28")
        add_long("RideOffAction+16")
        pass # RideOffActionCoupleEmotion
    # RideOffActionReact missing...
    # add_byte("RideOffAction+16")
    # add_int("RideOffAction+28")
    # add_unicode_str("unknown")
    elif action == 21:
        add_byte("RideOffAction+16")
        add_long("RideOffAction+16")
        add_unicode_str("unknown")
        pass # RideOffActionUseFunctionItem
    elif action == 22:
        add_byte("RideOffAction+16")
        add_unicode_str("unknown")
        add_int("RideOffAction+32")
        pass # RideOffActionNurturing
    elif action == 23:
        add_byte("RideOffAction+16")
        pass # RideOffActionGroggy
    elif action == 24:
        add_byte("RideOffAction+16")
        pass # RideOffActionUnRideSkill
    elif action == 25:
        add_byte("RideOffAction+16")
        add_long("RideOffAction+16")
        add_byte("RideOffAction+40")
        add_int("RideOffAction+44")
        pass # RideOffActionUseGlideItem
    elif action == 26:
        add_byte("RideOffAction+16")
        pass # RideOffActionHideAndSeek
elif f == 2:
    add_int("PlayerObjectId")
    add_int("MountId")
    add_long("MountUid")
elif f == 3:
    add_int("PlayerObjectId")
    with Node("sub_C04B70"):
        add_int("Unknown")
        add_byte("Unknown")
elif f == 4:
    add_int("PlayerObjectId")
    add_int("unknown")
elif f == 5:
    add_int("PlayerObjectId")
