from script_api import *

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

f = AddByte("Function")
if f == 0: # create listing
    DecodeMatchPartyRecruit()
elif f == 1: # cancel listing
    AddLong("PartyId")
elif f == 2: # load listings
    count = AddInt("count")
    for i in range(count):
        b = AddBool("IsListed")
        if b:
            DecodeMatchPartyRecruit()
elif f == 4: # error notice
    AddByte("Type")
    AddInt("code")
