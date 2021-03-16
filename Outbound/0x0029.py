from script_api import *

f = add_byte("Function")

if f == 2: # start quest (talk npc)
    add_int("QuestId")
    add_int("NpcObjectId")
elif f == 4: # complete quest
    add_int("QuestId")
    add_int("NpcObjectId")
    add_int("Unknown")
elif f == 6: # abandon
    add_int("QuestId")
elif f == 8: # get quests for map?
    count = add_int("count")
    for i in range(count):
        add_int("QuestId")
elif f == 14: # using "move to map"
    add_int("QuestId")
    add_short("Unknown") # not sure
elif f == 24: # claim navigator
    add_int("Unnknown") # 70000018
elif f == 26: # exploration reward
    add_int("StarAmount")
