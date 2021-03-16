from script_api import *

f = add_byte("function")
if f == 7:
    add_field("UserSkipped")
elif f == 10: # using computer
    add_int("CubeId") # 130304 when FunctionCubeName=4_130304
elif f == 12: # save script computer
    add_int("CubeId")
    add_str("scriptxml")
