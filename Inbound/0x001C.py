from script_api import *
from common import *

AddInt("ObjectId")
count = AddByte("Count")
for i in range(count):
    DecodeSyncState()
