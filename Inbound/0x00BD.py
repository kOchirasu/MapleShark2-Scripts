from script_api import *

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

f = add_byte("Function")
if f == 0: # create listing
    decode_match_party_recruit()
elif f == 1: # cancel listing
    add_long("PartyId")
elif f == 2: # load listings
    count = add_int("count")
    for i in range(count):
        b = add_bool("IsListed")
        if b:
            decode_match_party_recruit()
elif f == 4: # error notice
    add_byte("Type")
    add_int("code")
