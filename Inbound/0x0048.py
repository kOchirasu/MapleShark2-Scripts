from script_api import *
from common import *

f = add_byte("function")

add_int("BuffedObjectId")
add_int("BuffObjectId")
add_int("BuffOwnerObjectId")
if f == 0: # add_itional effect
    decode_additional_effect()
    add_long("Unknown") # 0
elif f == 1: # buff expired
    pass # none
elif f == 2: # skill buff effect (animation?)
    add_int("Unknown") # 1
    decode_additional_effect()
