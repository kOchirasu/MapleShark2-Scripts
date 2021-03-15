from script_api import *

f = AddByte("Function")
if f == 0: # Reuqest load
    AddByte("Function")
    AddInt("MapCode") # 102 = Victoria, 103 = Karkar, 105 = Kritias
else: # Request populations
    AddInt("MapCode") # 102 = Victoria, 103 = Karkar, 105 = Kritias
