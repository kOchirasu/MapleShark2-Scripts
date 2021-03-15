from script_api import *

f = AddByte("Function")

if f == 0:
    AddInt("Unknown")
elif f == 1: # Talking to npc with quests
    AddInt("NpcObjectId?")
    count = AddInt("Count")
    for i in range(count):
        AddInt("QuestId")
elif f == 2: # start quest
    AddInt("QuestId")
    AddLong("StartTime")
    AddByte("Started") # 1 (only set immediately after starting quest?)
    AddInt("Unknown")
elif f == 3: # exploration goal (1/1)
    AddInt("Unknown") # 72000145
    # maybe call on quest object + 68
    AddInt("Unknown") # 1
    AddInt("Unknown") # 1
elif f == 4: # complete (exploration goal, navigator?)
    AddInt("QuestId")
    AddInt("Unknown") # 1
    AddLong("CompletionTime")
elif f == 5:
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 6: # abandon
    AddInt("QuestId")
elif f == 7:
    count = AddInt("Count")
    for i in range(count):
        AddInt("Unknown")
elif f == 9:
    AddInt("Unknown")
    AddByte("Unknown")
elif f == 28:
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 21: # start load #0
    AddInt("Unknown") # something like count??
    AddInt("Unknown")
elif f == 22: # load quests #3 (chunked 200)
    count = AddInt("Count")
    for i in range(count):
        with Node("Quest " + str(i)):
            AddInt("QuestId")
            AddInt("State") # 1 = started, 2 = completed?
            AddInt("CompletionCount?")
            AddLong("StartTime")
            AddLong("EndTime")
            AddByte("Accepted")
            count2 = AddInt("Count")
            for j in range(count2):
                # I think this is used for keeping track of condition progress
                AddInt("ConditionCounter")
elif f == 23: # load quest ids #4?
    count = AddInt("Count")
    for i in range(count):
        AddInt("Unknown")
elif f == 25:
    AddLong("Unknown")
elif f == 26: # exploration reward
    AddInt("StarAmount")
elif f == 30:
    pass # none
elif f == 31: # load quest ids #1
    AddByte("Unknown")
    count = AddInt("Count")
    for i in range(count):
        AddInt("Unknown")
elif f == 32: # load quest ids #2
    AddByte("Unknown")
    count = AddInt("Count")
    for i in range(count):
        AddInt("Unknown")
elif f == 34 or f == 35: # (SidePopupTalkParam)
    AddShort("Unknown")
elif f == 38:
    pass # none
