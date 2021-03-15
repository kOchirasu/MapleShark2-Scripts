from script_api import *

f = AddByte("function")

if f == 4: # toggle use function cube
    AddUnicodeString("FunctionCubeName")
    AddBool("Using?")
elif f == 6: # finish using computer
    AddUnicodeString("FunctionCubeName")
