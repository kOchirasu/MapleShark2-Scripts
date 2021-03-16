from script_api import *
from common import *

def sub_5B9350():
    add_long("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_unicode_str("UnknownStr")
    add_byte("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_long("Unknown")
    add_unicode_str("UnknownStr")
    add_long("Unknown")

def decode_unknown_info():
    count = add_int("Count")
    for j in range(count):
        with Node("Entry " + str(j)):
            add_int("Unknown")
            add_byte("Unknown")

def decode_match_party_recruit():
    with Node("PartyListing", True):
        add_long("PartyId")
        add_int("SomeId") # increments somewhat
        add_int("Unknown")
        add_int("Unknown")
        add_unicode_str("PartyName")
        add_bool("IsPublic")
        add_int("MemberCount")
        add_int("MaxMembers")
        add_long("LeaderAccountId")
        add_long("LeaderCharacterId")
        add_unicode_str("LeaderName")
        add_long("CreationTime")
    

f = add_byte("function")
if f == 0:
    add_byte("Type")
    add_unicode_str("name")
elif f == 2: # joined party #1
    decode_player()
    decode_unknown_info()
elif f == 3: # left party (BROADCAST)
    add_long("CharacterId")
    add_bool("Unknown")
elif f == 4: # kicked from party
    add_long("CharacterId")
elif f == 5:
    decode_player()
elif f == 6:
    add_long("Unknown")
elif f == 7: # left party 2 (OTHERS)
    pass # None
elif f == 8: # become leader
    add_long("CharacterId")
elif f == 9: # load party
    add_bool("offline")
    add_int("partyId")
    add_long("LeaderUid")
    count = add_byte("count")
    for i in range(count):
        with Node("Member " + str(i)):
            add_bool("Unknown")
            decode_player()
            decode_unknown_info()
    add_bool("Unknown")
    add_int("DungeonId?")
    add_bool("Unknown")
    b = add_bool("IsPartyListed")
    if b:
        decode_match_party_recruit()
elif f == 11: # party request
    add_unicode_str("name")
    add_int("partyId")
elif f == 12:
    add_long("CharacterId")
    decode_player()
    decode_unknown_info()
elif f == 13: # same 12 (updating party player)
    add_long("CharacterId")
    decode_player()
    decode_unknown_info()
elif f == 14:
    add_long("CharacterId")
    decode_unknown_info()
elif f == 15:
    add_long("Unknown")
    add_int("Unknown")
elif f == 18:
    add_long("Unknown")
    add_byte("Unknown")
elif f == 19: # joined party #3
    add_long("CharacterId")
    add_long("AccountId")
    add_int("Hp")
    add_int("Hp")
    add_short("Unknown")
elif f == 20: # notice
    add_unicode_str("str_const") # s_party_vote_expired|s_field_enteracne_party_notify_reset_dungeon|s_party_vote_rejected_kick_user
    add_unicode_str("str_const") # Field_Enterance_Reset_Dungeon
    add_unicode_str("Unknown")
elif f == 21:
    b = add_bool("Unknown")
    add_int("Unknown")
    if b:
        add_int("Unknown")
        count = add_int("count")
        for i in range(count):
            add_unicode_str("UnknownStr")
    else:
        add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
elif f == 25: # dungeon reset
    add_bool("startedDungeon")
    add_int("DungeonId?")
elif f == 26: # party finder
    # true = listed, false = cancel listing
    b = add_bool("IsListed")
    if b:
        decode_match_party_recruit()
elif f == 30: # search party/search party cancel
    # 1->1, 2->8, 3->11, 4->5, default->0 (sub_437040)
    add_byte("Type")
    b = add_bool("StartSearch") # false = cancel
    add_bool("Unknown") # must be true
    add_byte("Unknown")
elif f == 31:
    add_long("Unknown")
elif f == 35:
    add_long("Unknown")
elif f == 37:
    add_long("Unknown")
    add_unicode_str("UnknownStr")
elif f == 40:
    # This value is used as (x / 1000 + 1)
    add_int("Unknown")
elif f == 44: # IGN wants to join your party
    add_unicode_str("name")
elif f == 47: # start ready check
    add_bool("Unknown") # vote kick = 1
    add_int("ReadyCheckConst(34)") # 36 = vote kick
    add_long("timestamp now")
    count = add_int("PartyCount")
    for i in range(count):
        add_long("CharacterId " + str(i))
    count = add_int("ReadyCount")
    for i in range(count):
        add_long("CharacterId " + str(i))
    count = add_int("NotReadyCount")
    for i in range(count):
        add_long("CharacterId " + str(i))
elif f == 48: # not ready
    add_long("CharacterId")
    add_bool("IsReady")
elif f == 49: # ready check expired/completed
    pass # none
elif f == 54: # search party/search party cancel
    b = add_bool("StartSearch") # false = cancel
    add_bool("Unknown") # must be true
