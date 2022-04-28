''' NPC_NOTICE '''
from script_api import *

f = add_byte("function")
if f == 0:
    add_unicode_str("stringnpcai.xml key") # $Pinkbean_PogoStick$
    add_int("Duration?") # 9000
elif f == 1:
    add_int("NpcObjectId")
    add_unicode_str("kfm") # EffectService
elif f == 2:
    add_int("NpcObjectId")
    add_unicode_str("animation") # urn:gamebryo-animation:*
elif f == 3: # SidePopupTalkParam
    add_byte("Unknown")
    add_int("duration")
    add_str("Unknown")
    add_str("illust")
    add_str("sound")
    add_str("Unknown")
    add_unicode_str("message")
