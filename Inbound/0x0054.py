from script_api import *
from common import *

def sub_5B9350():
    AddLong("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddUnicodeString("UnknownStr")
    AddByte("Unknown")
    AddInt("Unknown")
    AddInt("Unknown")
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
    AddLong("Unknown")

def DecodeUnknownInfo():
    count = AddInt("Count")
    for j in range(count):
        with Node("Entry " + str(j)):
            AddInt("Unknown")
            AddByte("Unknown")

def DecodeMatchPartyRecruit():
    with Node("PartyListing", True):
        AddLong("PartyId")
        AddInt("SomeId") # increments somewhat
        AddInt("Unknown")
        AddInt("Unknown")
        AddUnicodeString("PartyName")
        AddBool("IsPublic")
        AddInt("MemberCount")
        AddInt("MaxMembers")
        AddLong("LeaderAccountId")
        AddLong("LeaderCharacterId")
        AddUnicodeString("LeaderName")
        AddLong("CreationTime")
    

f = AddByte("function")
if f == 0:
    AddByte("Type")
    AddUnicodeString("name")
elif f == 2: # joined party #1
    DecodePlayer()
    DecodeUnknownInfo()
elif f == 3: # left party (BROADCAST)
    AddLong("CharacterId")
    AddBool("Unknown")
elif f == 4: # kicked from party
    AddLong("CharacterId")
elif f == 5:
    DecodePlayer()
elif f == 6:
    AddLong("Unknown")
elif f == 7: # left party 2 (OTHERS)
    pass # None
elif f == 8: # become leader
    AddLong("CharacterId")
elif f == 9: # load party
    AddBool("offline")
    AddInt("partyId")
    AddLong("LeaderUid")
    count = AddByte("count")
    for i in range(count):
        with Node("Member " + str(i)):
            AddBool("Unknown")
            DecodePlayer()
            DecodeUnknownInfo()
    AddBool("Unknown")
    AddInt("DungeonId?")
    AddBool("Unknown")
    b = AddBool("IsPartyListed")
    if b:
        DecodeMatchPartyRecruit()
elif f == 11: # party request
    AddUnicodeString("name")
    AddInt("partyId")
elif f == 12:
    AddLong("CharacterId")
    DecodePlayer()
    DecodeUnknownInfo()
elif f == 13: # same 12 (updating party player)
    AddLong("CharacterId")
    DecodePlayer()
    DecodeUnknownInfo()
elif f == 14:
    AddLong("CharacterId")
    DecodeUnknownInfo()
elif f == 15:
    AddLong("Unknown")
    AddInt("Unknown")
elif f == 18:
    AddLong("Unknown")
    AddByte("Unknown")
elif f == 19: # joined party #3
    AddLong("CharacterId")
    AddLong("AccountId")
    AddInt("Hp")
    AddInt("Hp")
    AddShort("Unknown")
elif f == 20: # notice
    AddUnicodeString("str_const") # s_party_vote_expired|s_field_enteracne_party_notify_reset_dungeon|s_party_vote_rejected_kick_user
    AddUnicodeString("str_const") # Field_Enterance_Reset_Dungeon
    AddUnicodeString("Unknown")
elif f == 21:
    b = AddBool("Unknown")
    AddInt("Unknown")
    if b:
        AddInt("Unknown")
        count = AddInt("count")
        for i in range(count):
            AddUnicodeString("UnknownStr")
    else:
        AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
elif f == 25: # dungeon reset
    AddBool("startedDungeon")
    AddInt("DungeonId?")
elif f == 26: # party finder
    # true = listed, false = cancel listing
    b = AddBool("IsListed")
    if b:
        DecodeMatchPartyRecruit()
elif f == 30: # search party/search party cancel
    # 1->1, 2->8, 3->11, 4->5, default->0 (sub_437040)
    AddByte("Type")
    b = AddBool("StartSearch") # false = cancel
    AddBool("Unknown") # must be true
    AddByte("Unknown")
elif f == 31:
    AddLong("Unknown")
elif f == 35:
    AddLong("Unknown")
elif f == 37:
    AddLong("Unknown")
    AddUnicodeString("UnknownStr")
elif f == 40:
    # This value is used as (x / 1000 + 1)
    AddInt("Unknown")
elif f == 44: # IGN wants to join your party
    AddUnicodeString("name")
elif f == 47: # start ready check
    AddBool("Unknown") # vote kick = 1
    AddInt("ReadyCheckConst(34)") # 36 = vote kick
    AddLong("timestamp now")
    count = AddInt("PartyCount")
    for i in range(count):
        AddLong("CharacterId " + str(i))
    count = AddInt("ReadyCount")
    for i in range(count):
        AddLong("CharacterId " + str(i))
    count = AddInt("NotReadyCount")
    for i in range(count):
        AddLong("CharacterId " + str(i))
elif f == 48: # not ready
    AddLong("CharacterId")
    AddBool("IsReady")
elif f == 49: # ready check expired/completed
    pass # none
elif f == 54: # search party/search party cancel
    b = AddBool("StartSearch") # false = cancel
    AddBool("Unknown") # must be true
