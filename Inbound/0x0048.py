''' BUFF '''
from script_api import *
from common import *

f = add_byte("function")

add_int("TargetObjectId")
add_int("BuffObjectId")
add_int("OwnerObjectId")
if f == 0: # add buff
    decode_additional_effect1()
    decode_additional_effect2()
elif f == 1: # buff expired (remove)
    pass # none
elif f == 2: # skill buff update (effect animation?)
    type = add_int("type")
    if type & 1: # bit 1
        decode_additional_effect1()
    if type & 2: # bit 2
        decode_additional_effect2()
