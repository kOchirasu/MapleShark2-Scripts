''' USER_CHAT '''
from script_api import *

add_long("AccountId")
add_long("CharacterId")
add_unicode_str("Name")
b = add_bool("Use StringId")
if b:
    add_int("StringId")
else:
    add_unicode_str("Message")
msgType = add_int("Type")
add_bool("Unknown")
add_int("Channel")
if msgType == 3: # whisper from
    add_unicode_str("Name")
elif msgType == 16 or msgType == 25: # super chat, wedding
    add_int("SuperChatItemId")
elif msgType == 20: # club chat
    add_long("ClubUid")
add_bool("Mentor related") # Mentor related (sub_CD0EF0): s_html_chat_img

'''
Type 10 (Command):
- IgnoreSkillCoolTime
- HandleRandomRegionSpawn
- CrashDump
- DumpPath
- SetPCBang
- Contract
- title
- SetQuestSeed
- AutoInstallEquipMent
'''
