from script_api import *
from common import *

f = AddByte("Function")
AddByte("State")
AddInt("ServerTick")
if f == 0:
    DecodeCoordF("Position")
elif f == 1:
    pass # nothing
