from script_api import *

f = add_byte("Function")
if f == 1:
    with Node("ChangeTitle", True):
        add_int("ObjectId")
        add_int("TitleId")
    
elif f == 2 or f == 4: # List unlocked titles?
    count = add_int("Count")
    for i in range(count):
        add_int("TitleId " + str(i))
elif f == 3 or f == 9:
    count = add_int("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            add_int("Unknown")
            add_byte("Unknown")
elif f == 8: # life skills / recipes
    count = add_int("Mining/Foraging Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            add_int("MasteryRecipe")
            add_int("Mastery")
    count = add_int("Ranching/Farming Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            add_int("MasteryRecipe")
            add_int("Unknown")
elif f == 10:
    count = add_int("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            add_short("entry#")
            add_int("Unknown")
elif f == 11:
    add_short("Unknown")
    add_int("Unknown")
elif f == 12:
    count = add_int("Count")
    for i in range(count):
        with Node("Entry " + str(i), True):
            add_int("Unknown")
            add_long("Timestamp")
elif f == 13:
    add_int("Unknown")
    add_long("Unknown")
else:
    add_int("Unknown")
