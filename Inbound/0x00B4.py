''' GAME_EVENT '''
from script_api import *

def decode_game_event_cli():
    pass # virtual call +16

f = add_byte("Function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            add_unicode_str("unknown") # GameEvent{0}Cli
            decode_game_event_cli()
elif f == 1:
    count = add_int("count")
    for i in range(count):
        add_unicode_str("unknown") # GameEvent{0}Cli
        decode_game_event_cli()
elif f == 2:
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
elif f == 3:
    count = add_int("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            add_unicode_str("unknown") # GameEvent{0}Cli
            decode_game_event_cli()
