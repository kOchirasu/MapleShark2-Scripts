from script_api import *

f = add_byte("Function")
if f == 0: # Reuqest load
    add_byte("Function")
    add_int("MapCode") # 102 = Victoria, 103 = Karkar, 105 = Kritias
else: # Request populations
    add_int("MapCode") # 102 = Victoria, 103 = Karkar, 105 = Kritias
