''' NOTICE '''
from script_api import *
from common import *

def IsMintNotice(flag):
    return flag & 0x10 != 0 # 00010000

def showMessage(flag):
    return flag & 0x200 != 0 # 001000000000

f = add_byte("function")
flag = add_short("flags")
decode_interface_text()
if IsMintNotice(flag): # Mint notice
    add_short("duration")

if f == 4:
    if not IsMintNotice(flag) and showMessage(flag):
        add_int("some id?")
elif f == 5:
    if flag == 0x40: # CMsgBoxData exactly
        pass # RequestQuit

''' Flags
B A 9 8 7 6 5 4 3 2 1
^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
| | | | | | | | | | |--Chat:setGmMessage
| | | | | | | | | |----Ignored
| | | | | | | | |------
| | | | | | | |--------Ignored if some condition and set...
| | | | | | |----------Mint
| | | | | |------------
| | | | |--------------CMsgBoxData
| | | |----------------CMsgBoxData + s_msg_disconnect_kickuser
| | |------------------
| |--------------------showMessage, MessengerData::TalkLog
|----------------------Chat:appendWarningMessage2

ChatTypes (these are hardcoded so you can't control here)
1  appendWarningMessage
2  appendWarningMessage2
3  appendInfoMessage
4  appendInfoMessage2
5  appendQuestMessage
6  setGmMessage
7  setFieldName
8  appendLetterMessage
9  appendEmergencyMessage
10 appendInteractMessage
11 appendGuildMegaphone
'''
