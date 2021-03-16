from script_api import *

# SendServerEnter
add_int("session id")
add_long("char id")
add_short("Unknown")
add_long("Exp")
add_long("RestExp")
add_long("Mesos")
add_long("Merets")
with Node("Merets 1"):
    add_long("Merets")
    add_long("GameMerets")
with Node("Merets 2"):
    add_long("GameMerets")
    add_long("EventMerets")
add_long("ValorToken")
add_long("Treva")
add_long("Rue")
add_long("HaviFruit")
add_long("Unknown")
add_long("Unknown")
add_long("Unknown")
add_long("Unknown")
add_long("MesoToken")
add_unicode_str("Profile URL")
add_byte("Unknown")
add_byte("Unknown")
with Node("Hidden Unlocked Maps?"):
    count = add_short("Count")
    for i in range(count):
        add_int("MapId")
with Node("Unlocked Maps"):
    count = add_short("Count")
    for i in range(count):
        add_int("MapId")
add_long("Unknown")
add_unicode_str("String")
add_unicode_str("maple news url")
add_unicode_str("String")
add_unicode_str("text-nx-cache url")
add_unicode_str("String")
