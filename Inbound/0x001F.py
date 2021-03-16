from script_api import *

f = add_byte("Function")
if f == 0:
    count = add_int("Count")
    for i in range(count):
        with Node("Emote " + str(i)):
            add_int("Unk")
            add_int("Unk")
            add_long("Unk")
