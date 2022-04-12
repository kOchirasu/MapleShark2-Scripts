''' MASSIVE_EVENT '''
from script_api import *

def decode_interface_text():
    b = add_bool("multiString")
    add_int("unknown")
    if b:
        add_int("unknown")
        count = add_int("count")
        for i in range(count):
            add_unicode_str("unknown")
    else:
        add_unicode_str("unknown")

f = add_byte("function")
if f == 0: # round ui
    add_int("Round")
    add_int("MaxRound")
    add_int("MinRound")
    add_int("VerticalOffset")
elif f == 1: # count ui
    # implicit: m_subType: 8
    add_unicode_str("m_text")
    add_int("m_stepNum") # round
    add_int("Count") # multiplied by 1000 and added to time
    add_int("m_unknown") # 1
elif f == 2: # banner ui
    add_byte("m_subType") # 0,1,2,5,6
    add_unicode_str("m_text")
    add_int("m_duration")
elif f == 3: # ui event introduce
    # implicit: m_subType: 6
    decode_interface_text()
    add_int("m_duration")
elif f == 4:
    # implicit: m_subType: 8
    decode_interface_text()
    add_int("m_stepNum")
    add_int("Count") # multiplied by 1000 and added to time
    add_int("m_unknown") # 1
elif f == 5:
    # implicit: m_subType: 2
    decode_interface_text()
    add_int("m_duration")
elif f == 6:
    # implicit: m_subType: 1
    decode_interface_text()
    add_int("m_duration")
elif f == 7: # start round popup
    add_int("round")
    b = add_bool("finalRound") # b ? onFinalRound : onRound
    add_int("m_duration")
elif f == 8:
    # implicit: m_stepNum: 0, m_text: s_pvp_ffa_triple_kill, m_unknown: 2
    add_int("Count") # multiplied by 1000 and added to time
