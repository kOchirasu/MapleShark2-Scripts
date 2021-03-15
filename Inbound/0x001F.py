from script_api import *

f = AddByte("Function")
if f == 0:
    count = AddInt("Count")
    for i in range(count):
        with Node("Emote " + str(i)):
            AddInt("Unk")
            AddInt("Unk")
            AddLong("Unk")
