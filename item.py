from script_api import *
from common import *

# Basic Ids for forcing branch logic
CAP_ID = 11300000
HAIR_ID = 10200000
DECAL_ID = 10400000
PET_ID = 60000000

TEMPLATE_ITEM_IDS = [
    11050005, 11050006, 11300041, 11300042, 11300043, 11300044, 11300045, 11300046, 11300155, 11300156, 
    11300157, 11300158, 11300697, 11300698, 11300699, 11300700, 11400024, 11400025, 11400026, 11400027, 
    11400080, 11400081, 11400082, 11400083, 11400120, 11400121, 11400418, 11400419, 11400550, 11400551, 
    11400607, 11400608, 11401077, 11401078, 11500024, 11500025, 11500026, 11500027, 11500081, 11500082, 
    11500338, 11500339, 11500522, 11500523, 11500971, 11500972, 11600034, 11600035, 11700048, 11700049, 
    11700173, 11700174, 11850005, 11850008, 11850180, 12200016, 12200017, 12200092, 12200093, 12200327, 
    12200328, 12200331, 12200332, 13000070, 13100203, 13100319, 13200198, 13200314, 13300197, 13300310, 
    13400196, 13400309, 14000162, 14000272, 14100171, 14100284, 15000202, 15000315, 15100194, 15100310, 
    15200201, 15200314, 15300197, 15300310, 15400112, 15400296, 15500509, 15600509, 15600532, 50100189, 
    50100385, 50200381, 50200382, 50200398, 50200399, 50200440, 50200486, 50200487, 50200488, 50200489, 
    50200490, 50200649, 50200700, 50200701, 50200702, 50200703, 50200738, 50200739, 50200740, 50200741, 
    50200742, 50200743, 50200744, 50200745, 50200746, 50200747, 50200748, 50200749, 50200750, 50200751, 
    50200752, 50200753, 50200754, 50200755, 50200756, 50200787, 50200878, 50200879, 50200880, 50200881, 
    50200882, 50200883, 50200884, 50200885, 50400088, 50400089, 50400228, 50600045, 50600054, 50600060, 
    50600066, 50600072, 50600078, 50600084, 50600089, 50600090, 50600278]
BLUEPRINT_ITEM_ID = 35200000


def decode_equip_color():
    with Node("EquipColor"):
        add_int("Color1")
        add_int("Color2")
        add_int("Color3")
        add_int("ColorIndex")
        add_int("Unknown")

def decode_item_extra_data(id: int):
    with Node("ItemExtraData"):
        decode_equip_color()
        add_field(str(id // 100000))
        # Item positioning
        if id // 100000 == 113:
            with Node("Cap"):
                decode_coordF("Position1")
                decode_coordF("Position2")
                decode_coordF("Position3")
                decode_coordF("Position4")
                add_float("Unknown")
        elif id // 100000 == 102:
            with Node("Hair"):
                add_float("BackLength")
                decode_coordF("BackPosition1")
                decode_coordF("BackPosition2")
                add_float("FrontLength")
                decode_coordF("FrontPosition1")
                decode_coordF("FrontPosition2")
        elif id // 100000 == 104:
            with Node("Decal"):
                add_float("Position1")
                add_float("Position2")
                add_float("Position3")
                add_float("Position4")

def decode_stat_option(index: int): # StatOption
    with Node("StatOption " + str(index)):
        add_int("IntegerValue")
        add_float("FloatValue")

def decode_special_option(index: int): # SpecialOption
    with Node("SpecialOption " + str(index)):
        add_float("FloatValue")
        add_float("FloatValue")

def decode_item_stats(): # sub_00562910
    with Node("Stats"):
        add_bool("Unknown")
        for i in {"Constant", "Static", "Random", "Title"}:
            with Node(i + "Stats"):
                count = add_short(i + "StatOptionCount")
                for j in range(count):
                    add_short("StatType")
                    decode_stat_option(j)
                count = add_short(i + "SpecialOptionCount")
                for j in range(count):
                    add_short("StatType")
                    decode_special_option(j)
            add_int("Unknown")

        for i in range(5):
            with Node("Empowerment Stats " + str(i)):
                count = add_short("EmpowermentStatOptionCount")
                for j in range(count):
                    add_short("StatType")
                    decode_stat_option(j)
                count = add_short("EmpowermentSpecialOptionCount")
                for j in range(count):
                    add_short("StatType")
                    decode_special_option(j)
            add_int("Unknown")

def decode_item_enchant(): # sub_0054C2B0
    with Node("ItemEnchant", True):
        add_int("Enchants")
        add_int("EnchantExp")
        add_byte("EnchantBasedChargeExp")
        add_long("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_bool("CanRepackage")
        add_int("EnchantCharges")

        with Node("EnchantStats"):
            count = add_byte("EnchantStatCount")
            for i in range(count):
                add_int("StatType")
                decode_stat_option(i)

def decode_item_limitbreak(): # sub_0066F520
    with Node("LimitBreak", True):
        add_int("LimitBreakLevel")
        with Node("LimitBreakStatOption"):
            count = add_int("LimitBreakStatOptionCount")
            for i in range(count):
                add_short("StatType")
                decode_stat_option(i)
        with Node("LimitBreakSpecialOption"):
            count = add_int("LimitBreakSpecialOptionCount")
            for i in range(count):
                add_short("StatType")
                decode_special_option(i)

def decode_ugc_item_look(): # CUgcItemLook
    with Node("CUgcItemLook"):
        add_long("Uid")
        add_unicode_str("UUID")
        add_unicode_str("ItemName")
        add_byte("Unknown")
        add_int("Unknown")
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("CharacterName")
        add_long("CreationTime")
        add_unicode_str("UGC Url")
        add_byte("Unknown")

def decode_ugc_item_music_score(): # CUgcItemMusicNote
    with Node("CUgcItemMusicNote"):
        add_long("unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_str("unknown")
        add_int("Unknown")
        add_long("unknown")
        add_long("unknown")
        add_unicode_str("unknown")

def decode_blueprint_item_data(): # BlueprintItemData
    with Node("BlueprintItemData"):
        add_long("unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_long("unknown")
        add_int("Unknown")
        add_long("unknown")
        add_long("unknown")
        add_unicode_str("unknown")

def decode_badge(id: int):
    with Node("Badge"):
        add_byte("Unknown")
        add_byte("BadgeType")
        add_unicode_str("BadgeIdStr")
        if id == 70100000: ## PetSkinBadge
            add_int("PetSkinId")
        elif id == 70100001: ## Transparency
            with Node("Transparency"):
                add_bool("Headgear")
                add_bool("Eyewear")
                add_bool("Top")
                add_bool("Bottom")
                add_bool("Cape")
                add_bool("Earrings")
                add_bool("Face")
                add_bool("Gloves")
                add_bool("Unknown")
                add_bool("Shoes")

def decode_item_music_score():
    with Node("MusicScore"):
        add_int("ScoreLength")
        add_int("Instrument")
        add_unicode_str("ScoreTitle")
        add_unicode_str("Author")
        add_int("Unknown (1)")
        add_long("AuthorCharacterId")
        add_byte("IsLocked")
        add_long("Unknown")
        add_long("Unknown")

def decode_item_pet():
    with Node("Pet"):
        add_unicode_str("PetName")
        add_long("PetExp")
        add_int("Unknown")
        add_int("PetLevel")
        add_byte("Unknown")

def decode_item_transfer():
    with Node("Transfer"):
        add_int("TransferFlag")
        add_bool("MailReceived")
        add_int("Remaining Trades")
        add_int("Remaining Repackage Count")
        add_byte("Unknown")
        add_bool("Unknown")
        f = add_byte("IsBound")
        if f != 0:
            decode_item_binding()

def decode_gem_sockets():
    with Node("GemSockets", True):
        add_byte("MaxSockets")
        count = add_byte("TotalSockets")
        for i in range(count):
            isUnlocked = add_bool("unlocked socket")
            if isUnlocked:
                decode_gemstone()

def decode_gemstone():
    with Node("Gemstone"):
        add_int("GemstoneItemId")
        # TSocketGemStoneBind
        isBound = add_bool("Bound")
        if isBound:
            decode_item_binding()
        # TSocketGemStoneLock
        b = add_bool("IsLocked")
        if b:
            add_bool("IsLocked")
            add_long("UnlockTime")

def decode_item_couple_info():
    b = add_long("PairedCharacterId")
    if b != 0:
        add_unicode_str("PairedName")
        add_bool("Unknown")

def decode_item_binding():
    add_long("BoundToCharId")
    add_unicode_str("BoundToName")

def decode_item(id: int):
    with Node("Item: " + str(id)):
        add_int("Amount")
        add_int("Unknown")
        add_int("Unknown")
        add_long("CreationTime")
        add_long("ExpiryTime")
        add_long("Unknown")
        add_int("TimesChangedAttribute")
        add_int("RemainingUses")
        add_byte("IsLocked")
        add_long("UnlockTime")
        add_short("GlamorForges")
        add_bool("Unknown")
        add_int("Unknown")

        decode_item_extra_data(id)
        decode_item_stats()
        decode_item_enchant()
        decode_item_limitbreak()

        if id in TEMPLATE_ITEM_IDS or id == BLUEPRINT_ITEM_ID:
            decode_ugc_item_look()
            decode_blueprint_item_data()
        # Pet
        if id // 100000 == 600 or id // 100000 == 610 or id // 100000 == 611 or id // 100000 == 629:
            decode_item_pet()
        # Music Score
        if id // 100000 == 351:
            decode_item_music_score()
        # Badge
        if id // 1000000 == 70:
            decode_badge(id)

        decode_item_transfer()
        decode_gem_sockets()
        decode_item_couple_info()
        decode_item_binding()

def decode_cube_item_info():
    with Node("CubeItemInfo"):
        add_int("ItemId")
        add_long("ItemUid")
        add_long("Unknown")
        b = add_bool("IsUgc")
        if b:
            decode_ugc_item_look()

def decode_item_entity():
    with Node("ItemEntity"):
        add_int("ItemId")
        add_short("Rarity")
        add_int("Amount")
        add_bool("Unknown")
        add_bool("Unknown")
        add_bool("Unknown")
        add_bool("Unknown")