from script_api import *
from common import *

# Request 0x0025 08 (SendJob)
# Response This packet
AddInt("ObjectId")
f = AddByte("function") # 2 for awakening?
if f != 0:
    DecodeSkillTree()
