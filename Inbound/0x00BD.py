''' MATCH_PARTY '''
from script_api import *

def decode_match_party_recruit():
    with Node("CMatchPartyRecruit", True):
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
    # s_partysearch_complete_register_membersearch
elif f == 1: # cancel listing
    add_long("PartyId")
    # s_partysearch_complete_remove_membersearch
elif f == 2: # load listings
    count = add_int("count")
    for i in range(count):
        b = add_bool("IsListed")
        if b:
            decode_match_party_recruit()
    # s_partysearch_err_search_result_empty
elif f == 4: # error notice
    category = add_byte("category")
    message = add_int("message")
    '''
    if message == 2:
        pass # s_partysearch_err_server_db
    elif message == 13 or message == 14 or message == 15:
        pass # s_partysearch_err_server_already_register
    elif message == 99:
        pass # s_partysearch_err_server_lastaction
    elif message == 101:
        pass # s_partysearch_err_server_not_chief
    elif message == 109:
        pass # s_partysearch_err_server_blocked
    elif message == 110:
        pass # s_partysearch_err_server_max_member

    if category == 0:
        if message == 102:
            pass # s_partysearch_err_server_invalid_type
        elif message == 104:
            pass # s_partysearch_err_server_in_party
        elif message == 105:
            pass # s_partysearch_err_server_already_register
        elif message == 108:
            pass # s_partysearch_err_server_banword_title
        elif message == 111:
            pass # s_partysearch_err_server_party_invited
    elif category == 1:
        if message == 103:
            pass # s_partysearch_err_server_registring
        elif message == 106:
            pass # s_partysearch_err_server_not_find_recruit
    elif category == 2:
        if message == 108:
            pass # s_partysearch_err_server_banword_findword
    # Default error:
    # s_partysearch_err_server_code
    '''
