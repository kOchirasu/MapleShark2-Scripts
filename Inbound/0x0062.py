from script_api import *

f = AddByte("function")
if f == 0: # round ui
    AddInt("Round")
    AddInt("MaxRound")
    AddInt("MinRound")
    AddInt("VerticalOffset")
elif f == 1: # count ui
    AddUnicodeString("name")
    AddInt("Round")
    AddInt("Count")
    AddInt("Unknown") # 1
elif f == 2: # banner ui
    AddByte("Type")
    AddUnicodeString("Name")
    AddInt("duration")
elif f == 3: # ui event introduce
    AddInt("Number")
    AddBool("IsFinal") # ignores number
    AddInt("Duration")
elif f == 7: # start round popup
    AddInt("round")
    AddBool("IsFinal?")
    AddInt("duration")
