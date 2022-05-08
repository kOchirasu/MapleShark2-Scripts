''' MESSENGER_BROWSER '''
from script_api import *
from item import *

# <A HREF="event:itemTooltip,2867553202885834708,3,2867553202885834708,20000004,1">[Elixir]</A>
# event:itemTooltip,{ItemUid},{Type},{2},{ItemId},{Rarity}
# event:achieveTooltip,{0},{1},{2},{3},{4}
# event:billDialog,{0},{1},{2},{3},{4}
# event:searchFromMeratmarket,{0},{1},{2},{3},{4},{5},{6} <- 6 optional?

''' Type
if IsMeso: # Id in [90000001, 90000002, 90000003]
    s_msg_item_open_item_announce_to_world_meso
if IsMeret: # Id in [90000004, 90000011, 90000015, 90000016]
    s_msg_item_open_item_announce_to_world_merat

1: s_itemenchant_success_notice
2: s_itemremake_chat_maxoption
3: s_msg_item_open_item_announce_to_world
4: s_card_reverse_game_reward_notice
5: s_item_merge_chat_maxoption
6: s_msg_item_identified_item_announce_to_world
'''

count = add_int("count")
for i in range(count):
    add_long("ItemUid")
    id = add_int("ItemId")
    add_int("Rarity")
    decode_item(id)
