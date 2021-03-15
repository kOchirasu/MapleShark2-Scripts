from script_api import *

f = AddByte("function")
if f == 7:
    AddField("UserSkipped")
elif f == 10: # using computer
    AddInt("CubeId") # 130304 when FunctionCubeName=4_130304
elif f == 12: # save script computer
    AddInt("CubeId")
    AddString("scriptxml")
