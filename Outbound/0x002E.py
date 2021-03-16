from script_api import *

f = add_byte("function")

if f == 4: # toggle use function cube
    add_unicode_str("FunctionCubeName")
    add_bool("Using?")
elif f == 6: # finish using computer
    add_unicode_str("FunctionCubeName")
