''' SERVER_ENTER '''
from script_api import *

# SendServerEnter
add_int("PlayerObjectId")
add_long("PlayerId")
add_short("Channel") # related to s_msg_chatting_changechannel
add_long("Exp")
add_long("RestExp")
add_long("Mesos")
with Node("Merets"):
    add_long("Merets")
    add_long("Merets2")
    add_long("GameMerets")
    add_long("GameMerets2")
add_long("EventMerets")
add_long("ValorToken")
add_long("Treva")
add_long("Rue")
add_long("HaviFruit")
add_long("ReverseCoin")
add_long("MentorToken")
add_long("MenteeToken")
add_long("StarPoint")
add_long("MesoToken")
add_unicode_str("Profile URL")
add_byte("Unknown") # SurvivalContents03 related
add_byte("Unknown")
with Node("Unlocked Maps"):
    count = add_short("Count")
    for i in range(count):
        add_int("MapId")
with Node("Unlocked Taxis"):
    count = add_short("Count")
    for i in range(count):
        add_int("MapId")
add_long("Unknown")
add_unicode_str("String")
add_unicode_str("maple news url")
add_unicode_str("String")
add_unicode_str("text-nx-cache url")
add_unicode_str("String")
