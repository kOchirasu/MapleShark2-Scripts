from script_api import *

# Caught fish and got box (Manual)
# 03 88 96 98 00 02 00 00 00 02 00 15 00
# 08 88 96 98 00 01 00 00 00 01 00 88 96 98 00 01 00 00 00 00 00 00 00 01 00 00 00
# 05 [01 00 00 00] [C7 52 87 03] [01 00]
# 04 01 [01 00 00 00] [F6 FC 12 00] [81 96 98 00] [19 00 00 00] [40 1F 00 00] [01 00]

# Cuaght fish automatically
# 08 88 96 98 00 01 00 00 00 01 00 88 96 98 00 02 00 00 00 00 00 00 00 01 00 00 00
# 05 01 00 00 00 67 C5 C9 01 01 00
# 04 01 01 00 00 00 F6 FC 12 00 81 96 98 00 19 00 00 00 40 1F 00 00 01 00

# Failed
# 04 01 01 00 00 00 F6 FC 12 00 81 96 98 00 19 00 00 00 40 1F 00 00 01 00

f = AddByte("Function")
if f == 0:
    AddLong("RodItemUid")
elif f == 3:
    AddInt("FishId")
    AddInt("Unknown") # 2
    AddShort("Unknown") # 2 (1)
    AddShort("Unknown") # 21 (1)
elif f == 4:
    AddByte("Unknown")
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i)):
            AddInt("Unknown")
            AddInt("Unknown") # 10000001
            AddInt("Unknown") # 25
            AddInt("Unknown") # 8000 (15000)
            AddShort("Unknown") # 1
elif f == 5: # Caught item
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i)):
            AddInt("ItemId")
            AddShort("Amount")
elif f == 7: # Load fising book
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i)):
            AddInt("FishId")
            AddInt("Total Caught")
            AddInt("Total Prized Fish")
            AddInt("Largest Fish Size")
elif f == 8:
    AddInt("FishId")
    AddInt("FishSize")
    b = AddByte("Success") # Update log on success
    AddByte("Unknown")
    if b != 0:
        AddInt("FishId")
        AddInt("Total Caught")
        AddInt("Total Prized Fish")
        AddInt("Largest Fish Size")

elif f == 9:
    AddByte("1?")
    AddInt("ServerTicks")
