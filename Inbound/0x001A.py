from script_api import *

def DecodeDungeonRecordCli():
    AddInt("DungeonRoomId")
    AddLong("ClearDate") # no minutes
    AddByte("Unknown")
    AddByte("Unknown")
    AddLong("Unknown")
    AddByte("Unknown")
    AddByte("Unknown")
    AddLong("Unknown")
    AddInt("Unknown")
    AddShort("Unknown")
    AddLong("Unknown")
    AddShort("Unknown")
    AddByte("Unknown")

def DecodeDungeonRankReward():
    AddInt("DungeonRoomId")
    AddInt("Unknown")
    AddLong("Unknown")

f = AddByte("Function")
if f == 5:
    count = AddInt("Count")
    for i in range(count):
        with Node("DungeonRecord " + str(i)):
            AddInt("DungeonRoomId")
            DecodeDungeonRecordCli()
elif f == 6: # DungeonRecordCli
    DecodeDungeonRecordCli()
elif f == 7:
    AddByte("Type")
    AddInt("Unknown")
    # some string notice?
elif f == 9: # UIDungeonExpenseRewardDialog
    AddInt("Unknown")
    AddInt("Unknown")
elif f == 11: # UIDungeonClosingPhotoDialog
    AddByte("Unknown")
    count = AddInt("Count")
    for i in range(count):
        AddLong("CharacterId")
        AddInt("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
elif f == 12: # UI related
    pass # none
elif f == 19: # error
    AddInt("Type") # 8 = dungeon expired
    AddInt("Unknown")
    # server sends additional useless int
elif f == 20:
    count = AddInt("Count")
    for i in range(count):
        with Node("RankReward " + str(i)):
            AddInt("DungeonRoomId")
            DecodeDungeonRankReward()
elif f == 21: # DungeonRankReward
    DecodeDungeonRankReward()
elif f == 23:
    AddLong("Timestamp")
    AddLong("CharacterId")
