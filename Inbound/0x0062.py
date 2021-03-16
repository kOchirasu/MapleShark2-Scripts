from script_api import *

f = add_byte("function")
if f == 0: # round ui
    add_int("Round")
    add_int("MaxRound")
    add_int("MinRound")
    add_int("VerticalOffset")
elif f == 1: # count ui
    add_unicode_str("name")
    add_int("Round")
    add_int("Count")
    add_int("Unknown") # 1
elif f == 2: # banner ui
    add_byte("Type")
    add_unicode_str("Name")
    add_int("duration")
elif f == 3: # ui event introduce
    add_int("Number")
    add_bool("IsFinal") # ignores number
    add_int("Duration")
elif f == 7: # start round popup
    add_int("round")
    add_bool("IsFinal?")
    add_int("duration")
