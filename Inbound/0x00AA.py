from script_api import *

f = AddByte("Function")
if f == 1:
    with Node("ChangeTitle", True):
        AddInt("ObjectId")
        AddInt("TitleId")
    
elif f == 2 or f == 4: # List unlocked titles?
    count = AddInt("Count")
    for i in range(count):
        AddInt("TitleId " + str(i))
elif f == 3 or f == 9:
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            AddInt("Unknown")
            AddByte("Unknown")
elif f == 8: # life skills / recipes
    count = AddInt("Mining/Foraging Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            AddInt("MasteryRecipe")
            AddInt("Mastery")
    count = AddInt("Ranching/Farming Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            AddInt("MasteryRecipe")
            AddInt("Unknown")
elif f == 10:
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            AddShort("entry#")
            AddInt("Unknown")
elif f == 11:
    AddShort("Unknown")
    AddInt("Unknown")
elif f == 12:
    count = AddInt("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            AddInt("Unknown")
            AddLong("Timestamp")
elif f == 13:
    AddInt("Unknown")
    AddLong("Unknown")
else:
    AddInt("Unknown")
