from script_api import *

f = AddByte("Function")

if f == 2: # start quest (talk npc)
    AddInt("QuestId")
    AddInt("NpcObjectId")
elif f == 4: # complete quest
    AddInt("QuestId")
    AddInt("NpcObjectId")
    AddInt("Unknown")
elif f == 6: # abandon
    AddInt("QuestId")
elif f == 8: # get quests for map?
    count = AddInt("count")
    for i in range(count):
        AddInt("QuestId")
elif f == 14: # using "move to map"
    AddInt("QuestId")
    AddShort("Unknown") # not sure
elif f == 24: # claim navigator
    AddInt("Unnknown") # 70000018
elif f == 26: # exploration reward
    AddInt("StarAmount")
