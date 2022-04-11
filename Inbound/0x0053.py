''' QUEST '''
from script_api import *

f = add_byte("Function")

if f == 0:
    message = add_int("message")
    if message == 1:
        pass # s_quest_error_inventory_full
    elif message == 2:
        pass # s_quest_error_consume_fail
    elif message == 3:
        pass # s_quest_error_accept_fail
    elif message == 4:
        pass # s_quest_error_invalid_date
    elif message == 5:
        pass # s_quest_error_fail_complete_by_dead
    elif message == 7:
        pass # s_alliance_quest_completion_ticket_error
elif f == 1: # Talking to npc with quests
    add_int("NpcObjectId")
    count = add_int("Count")
    for i in range(count):
        add_int("QuestId")
elif f == 2: # start quest
    add_int("QuestId")
    add_long("StartTime")
    add_byte("Started") # 1 (only set immediately after starting quest?)
    add_int("Unknown")
elif f == 3: # exploration goal (1/1)
    add_int("Unknown") # 72000145
    # maybe call on quest object + 68
    add_int("Unknown") # 1
    add_int("Unknown") # 1
elif f == 4: # complete (exploration goal, navigator?)
    add_int("QuestId")
    add_int("Unknown") # 1
    add_long("CompletionTime")
elif f == 5:
    add_int("Unknown")
    add_int("Unknown")
elif f == 6: # abandon
    add_int("QuestId")
elif f == 7:
    count = add_int("Count")
    for i in range(count):
        add_int("Unknown")
elif f == 9:
    add_int("Unknown")
    add_byte("Unknown")
elif f == 18:
    add_int("field_D8")
    add_int("field_D4")
    add_int("field_DC")
elif f == 21: # start load #0
    add_int("Unknown") # something like count??
    add_int("Unknown")
elif f == 22: # load quests #3 (chunked 200)
    count = add_int("Count")
    for i in range(count):
        with Node("Quest " + str(i)):
            add_int("QuestId")
            add_int("State") # 1 = started, 2 = completed?
            add_int("CompletionCount?")
            add_long("StartTime")
            add_long("EndTime")
            add_byte("Accepted")
            count2 = add_int("Count")
            for j in range(count2):
                # I think this is used for keeping track of condition progress
                add_int("ConditionCounter")
elif f == 23: # load quest ids #4?
    count = add_int("Count")
    for i in range(count):
        add_int("QuestId")
elif f == 25:
    add_long("Unknown")
elif f == 26: # exploration reward
    add_int("StarAmount")
elif f == 30:
    pass # sub_C31060(8, 2, 1);
elif f == 31: # load quest ids #1
    add_bool("Unknown") # if true -> sub_C31060(9, 3, 1);
    count = add_int("Count")
    for i in range(count):
        add_int("Unknown")
elif f == 32: # load quest ids #2
    add_bool("Unknown") # if true -> sub_C31060(9, 3, 1);
    count = add_int("Count")
    for i in range(count):
        add_int("Unknown")
elif f == 34 or f == 35: # (SidePopupTalkParam)
    add_short("Unknown")
    # s_quest_alliance_accept_all_{0}
    # s_quest_alliance_complete_all_{0}
elif f == 38:
    pass # none
