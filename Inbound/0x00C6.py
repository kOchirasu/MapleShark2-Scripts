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

f = add_byte("Function")
if f == 0: # prepare fishing
    add_long("RodItemUid")
elif f == 1: # stop fishing
    pass
elif f == 2: # notice
    add_short("NoticeId")
elif f == 3: # increase mastery
    add_int("FishId")
    add_int("ExpGained") # 2
    add_int("Mastery Type")
elif f == 4: # load fishing tiles
    add_byte("Unknown")
    count = add_int("Tile Count")
    for i in range(count):
        with Node("Tile " + str(i)):
            add_int("CoordB")
            add_int("Unknown") # 10000001
            add_int("Unknown") # 25
            add_int("FishingTime") # 15000 - reducedTime (from rods/bait)
            add_short("Unknown") # 1
elif f == 5: # Caught item
    count = add_int("Count")
    for i in range(count):
        with Node("Entry " + str(i)):
            add_int("ItemId")
            add_short("Amount")
elif f == 7: # Load fising book
    count = add_int("Count")
    for i in range(count):
        with Node("Entry " + str(i)):
            add_int("FishId")
            add_int("Total Caught")
            add_int("Total Prized Fish")
            add_int("Largest Fish Size")
elif f == 8: # caught fish
    add_int("FishId")
    add_int("FishSize")
    b = add_byte("Success") # Update log on success
    add_byte("Unknown")
    if b != 0:
        add_int("FishId")
        add_int("Total Caught")
        add_int("Total Prized Fish")
        add_int("Largest Fish Size")
elif f == 9: # start fishing
    add_byte("FishingGameBool")
    add_int("ServerTicks")
