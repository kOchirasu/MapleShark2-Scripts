from script_api import *

def decode_dungeon_record_cli():
    add_int("DungeonRoomId")
    add_long("ClearDate") # no minutes
    add_byte("Unknown")
    add_byte("Unknown")
    add_long("Unknown")
    add_byte("Unknown")
    add_byte("Unknown")
    add_long("Unknown")
    add_int("Unknown")
    add_short("Unknown")
    add_long("Unknown")
    add_short("Unknown")
    add_byte("Unknown")

def decode_dungeon_rank_reward():
    add_int("DungeonRoomId")
    add_int("Unknown")
    add_long("Unknown")

f = add_byte("Function")
if f == 5:
    count = add_int("Count")
    for i in range(count):
        with Node("DungeonRecord " + str(i)):
            add_int("DungeonRoomId")
            decode_dungeon_record_cli()
elif f == 6: # DungeonRecordCli
    decode_dungeon_record_cli()
elif f == 7:
    add_byte("Type")
    add_int("Unknown")
    # some string notice?
elif f == 9: # UIDungeonExpenseRewardDialog
    add_int("Unknown")
    add_int("Unknown")
elif f == 11: # UIDungeonClosingPhotoDialog
    add_byte("Unknown")
    count = add_int("Count")
    for i in range(count):
        add_long("CharacterId")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
elif f == 12: # UI related
    pass # none
elif f == 19: # error
    add_int("Type") # 8 = dungeon expired
    add_int("Unknown")
    # server sends add_itional useless int
elif f == 20:
    count = add_int("Count")
    for i in range(count):
        with Node("RankReward " + str(i)):
            add_int("DungeonRoomId")
            decode_dungeon_rank_reward()
elif f == 21: # DungeonRankReward
    decode_dungeon_rank_reward()
elif f == 23:
    add_long("Timestamp")
    add_long("CharacterId")
