from script_api import *
from common import *

f = AddByte("function")

AddInt("BuffedObjectId")
AddInt("BuffObjectId")
AddInt("BuffOwnerObjectId")
if f == 0: # additional effect
    DecodeAdditionalEffect()
    AddLong("Unknown") # 0
elif f == 1: # buff expired
    pass # none
elif f == 2: # skill buff effect (animation?)
    AddInt("Unknown") # 1
    DecodeAdditionalEffect()
