from script_api import *
from common import *

f = AddByte("Function")
if f == 0:
    AddInt("MapId")
    AddByte("Unknown")
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    DecodeCoordF("Position")
    DecodeCoordF("Rotation")
    AddInt("Unknown")
