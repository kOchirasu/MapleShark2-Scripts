from script_api import *

def decode_coordF(str):
    with Node(str + "CoordF"):
        add_float("X")
        add_float("Y")
        add_float("Z")

def decode_coordS(str):
    with Node(str + "CoordS"):
        add_short("X")
        add_short("Y")
        add_short("Z")

def decode_equip_color():
    with Node("EquipColor"):
        add_int("Color1")
        add_int("Color2")
        add_int("Color3")
        add_int("ColorIndex")

def decode_skin_color():
    with Node("SkinColor"):
        add_int("Color1")
        add_int("Color2")

def decode_ugc_data(): # CUgcItemLook
    with Node("UgcData"):
        add_long("Unknown")
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

def decode_blueprint(): # BlueprintItemData
    with Node("Blueprint"):
        add_long("unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_long("unknown")
        add_int("Unknown")
        add_long("unknown")
        add_long("unknown")
        add_unicode_str("unknown")

def decode_cube_item_info():
    with Node("CubeItemInfo"):
        add_int("ItemId")
        add_long("ItemUid")
        add_long("Unknown")
        b = add_bool("IsUgc")
        if b:
            decode_ugc_data()

def decode_state_sync():
    with Node("StateSync", True):
        add_byte("state")
        add_byte("subState") # Assert(n <= 178)
        flag = add_byte("Flag")
        if (flag & 1) == 1: ## bit-1
            add_int("Unknown")
            add_short("Unknown")
        decode_coordS("Position")
        add_short("Rotation")
        u = add_byte("Animation3")
        # if u < 0???
        if u > 127:
            add_float("Unknown")
            add_float("Unknown")
        decode_coordS("")
        add_byte("Unknown") # Assert(n < 18)
        add_short("CoordS / 10")
        add_short("CoordS / 1000")
        if (flag & 2) == 2: ## bit-2
            decode_coordF("Unknown")
            add_unicode_str("UnknownStr")
        if (flag & 4) == 4: ## bit-3
            add_int("Unknown")
            add_unicode_str("UnknownStr")
        if (flag & 8) == 8: ## bit-4
            add_unicode_str("AnimationString?")
        if (flag & 16) == 16: ## bit-5
            add_int("Unknown")
            add_unicode_str("UnknownStr")
        if (flag & 32) == 32: ## bit-6
            add_int("Unknown")
            add_int("Unknown")
            add_byte("Unknown")
            decode_coordF("Unknown")
            decode_coordF("Unknown")
        add_int("Unknown")

def decode_item_stats(): # sub_00562910
    add_bool("Unknown")
    
    with Node("Stats"): # this is actually a loop range(9)
        with Node("Constant Stats"):
            count = add_short("ConstantStatOptionCount")
            for i in range(count):
                decode_stat_option(i)
            count = add_short("ConstantSpecialOptionCount")
            for i in range(count):
                decode_special_option(i)
        add_int("Unknown")

        with Node("Static Stats"):
            count = add_short("StaticStatOptionCount")
            for i in range(count):
                decode_stat_option(i)
            count = add_short("StaticSpecialOptionCount")
            for i in range(count):
                decode_special_option(i)
        add_int("Unknown")

        with Node("Random Stats"):
            count = add_short("RandonStatOptionCount")
            for i in range(count):
                decode_stat_option(i)
            count = add_short("RandomSpecialOptionCount")
            for i in range(count):
                decode_special_option(i)
        add_int("Unknown")

        with Node("Title Stats"):
            count = add_short("TitleStatOptionCount")
            for i in range(count):
                decode_stat_option(j)
            count = add_short("TitleSpecialOptionCount")
            for i in range(count):
                decode_special_option(i)
        add_int("Unknown")

        for i in range(5):
            with Node("Empowerment Stats " + str(i)):
                count = add_short("EmpowermentStatOptionCount")
                for j in range(count):
                    decode_stat_option(j)
                count = add_short("EmpowermentSpecialOptionCount")
                for j in range(count):
                    decode_special_option(j)
            add_int("Unknown")

def decode_item_enchant(): # sub_0054C2B0
    add_int("Enchants")
    add_int("EnchantExp")
    add_bool("EnchantBasedChargeExp")
    add_long("Unknown")
    add_int("Unknown")
    add_int("Unknown")
    add_bool("CanRepackage")
    add_int("EnchantCharges")

    with Node("EnchantStats"):
        count = add_byte("EnchantStatCount")
        for i in range(count):
            decode_stat_option(i)

def decode_item_limitbreak(): # sub_0066F520
    add_int("LimitBreakLevel")
    with Node("LimitBreakStatOption"):
        count = add_int("LimitBreakStatOptionCount")
        for i in range(count):
            decode_stat_option(i)
    with Node("LimitBreakSpecialOption"):
        count = add_int("LimitBreakSpecialOptionCount")
        for i in range(count):
            decode_special_option(i)

def decode_item(id):
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
        decode_equip_color()
        add_int("Unknown")
        # Item positioning
        if id / 100000 == 113:
            add_field("Cap Position", 13 * 4)
        elif id / 100000 == 102:
            add_field("Back Hair Position", 4 * 7)
            add_field("Front Hair Position", 4 * 7)
        elif id / 100000 == 104:
            add_field("Cosmetic Position", 4 * 4)
        
        decode_item_stats()
        decode_item_enchant()
        decode_item_limitbreak()

        #Testing UGC
        if id == 11400608 or id == 11500523 or id == 11600035:
            with Node("UGC", True):
                decode_ugc_data()
                decode_blueprint()

        # Pet
        if id / 100000 == 600 or id / 100000 == 610 or id / 100000 == 611 or id / 100000 == 629:
            with Node("Pet", True):
                add_unicode_str("PetName")
                add_long("PetExp")
                add_int("Unknown")
                add_int("PetLevel")
                add_byte("Unknown")

        # Music Score
        if id / 100000 == 351:
            with Node("MusicScore", True):
                add_int("ScoreLength")
                add_int("Instrument")
                add_unicode_str("ScoreTitle")
                add_unicode_str("Author")
                add_int("Unknown (1)")
                add_long("AuthorCharacterId")
                add_byte("IsLocked")
                add_field("Unknown", 16)

        # Badge
        if id / 1000000 == 70:
            with Node("Badge", True):
                add_byte("Unknown")
                add_byte("Unknown")
                add_unicode_str("BadgeIdStr")
                if id == 70100000: ## PetSkinBadge
                    add_int("PetSkinId")
                elif id == 70100001: ## Transparency
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

        add_int("TransferFlag")
        add_byte("???")
        add_int("remaining trades")
        add_int("Remaining Repackage Count")
        add_byte("???")
        add_byte("???")
        f = add_byte("IsBound")
        if f != 0:
            add_long("BoundToCharId")
            add_unicode_str("BoundToName")
        decode_gem_sockets()
        b = add_long("PairedCharacterId")
        if b != 0:
            add_unicode_str("PairedName")
            add_byte("Unknown")
        add_long("???")
        add_unicode_str("Unknown")

def decode_stat_option(index): # StatOption
    with Node("StatOption " + str(index)):
        add_short("StatType")
        add_int("IntegerValue")
        add_float("FloatValue")

def decode_special_option(index): # SpecialOption
    with Node("SpecialOption " + str(index)):
        add_short("StatType")
        add_float("FloatValue")
        add_float("FloatValue")

def decode_player():
    with Node("PlayerInfo"):
        add_long("AccountId")
        add_long("PlayerId")
        add_unicode_str("Name")
        add_byte("Gender") # 0 = male, 1 = female
        add_byte("Unknown")
        add_long("Unknown")

        add_int("Unknown")
        add_int("MapId")
        add_int("InstanceMapId") # Guess
        add_int("MapInstanceId") # Guess
        add_short("Level")
        add_short("ChannelId")
        add_int("JobCode")
        add_int("JobId")
        add_int("CurrentHp")
        add_int("MaxHp")
        add_short("Unknown")

        add_long("Unknown")
        add_long("StorageAccessTime")
        add_long("DoctorAccessTime")
        add_int("OutsideMapId")
        decode_coordF("OutsidePosition")
        add_int("GearScore")
        decode_skin_color()
        add_long("CreationTime")
        with Node("Trophy"):
            for i in range(3):
                add_int("Count")
        add_long("GuildUid")
        add_unicode_str("GuildName")
        add_unicode_str("Motto")
        add_unicode_str("ProfileUrl")

        # CharacterListClubParser
        with Node("Clubs"):
            count = add_byte("count")
            for i in range(count):
                b = add_byte("hasClub")
                if b == 1:
                    add_long("clubUid")
                    add_unicode_str("Club Name")

        add_byte("Unknown")
        with Node("LifeSkills"):
            add_int("Fishing???")
            add_int("Fishing")
            add_int("Instrument")
            add_int("Mining")
            add_int("Foraging")
            add_int("Ranching")
            add_int("Farming")
            add_int("Smithing")
            add_int("Handicrafts")
            add_int("Alchemy")
            add_int("Cooking")
            add_int("PetTaming")

        with Node("player->field_278->Decode()"):
            add_unicode_str("UnknownStr")
            add_long("SessionId")
            add_long("Unknown")
            add_long("Unknown")

        with Node("countA"):
            count = add_int("countA")
            for i in range(count):
                add_long("Unknown")

        add_byte("Unknown")
        add_bool("Unknown")
        add_long("Unknown")
        add_int("Unknown")
        add_int("Unknown")
        add_long("TimestampNow?")
        add_int("PrestigeLevel")
        add_long("LoginTimestamp?")

        # these are both related?
        count = add_int("countB")
        for i in range(count):
            add_long("Unknown")
        count = add_int("countC")
        for i in range(count):
            add_long("Unknown")

        add_short("Unknown")
        add_long("Unknown")

def decode_skill_tree():
    add_int("JobId")
    add_byte("Unknown (1)")
    add_int("JobGroupId")
    with Node("Skills"):
        for i in range(2):
            skillType = "Active Skills" if i == 0 else "Passive Skills"
            with Node(skillType, True):
                count = add_byte("Count")
                for j in range(count):
                    start_node("Skill " + str(j))
                    add_bool("NewlyEnabled")
                    b = add_bool("Enabled")
                    add_int("SkillId")
                    add_int("Skill Points")
                    add_bool("Unknown (0)")
                    end_node(b)
    add_byte("Unknown")
    add_byte("Unknown")

def decode_gem_sockets():
    add_byte("MaxSockets")
    count = add_byte("TotalSockets")
    for i in range(count):
        isUnlocked = add_bool("unlocked socket")
        if isUnlocked:
            decode_gemstone()

def decode_gemstone():
    with Node("Gemstone"):
        add_int("GemstoneItemId")
        isBound = add_bool("Bound")
        if isBound:
            add_long("CharacterId")
            add_unicode_str("Name")
        b = add_bool("UnknownFlag")
        if b:
            add_byte("Unknown")
            add_long("Unknown")

def decode_maid():
    add_long("MaidUid?")
    add_long("ItemUid")
    add_long("Timestamp")
    add_long("Timestamp")
    add_long("AccountId")
    add_int("MaidId") # 50800017
    add_int("NpcId") # 11000785
    add_bool("IsDeployed")
    add_int("Mood")
    add_int("Level")
    add_int("Closeness")
    add_long("ExpirationTimestamp")
    count2 = add_int("count")
    for j in range(count2):
        add_long("Unknown")
    # Diff sub
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")
    add_unicode_str("UnknownStr")

def decode_additional_effect1():
    with Node("additionalEffect", True):
        add_int("StartServerTick")
        add_int("EndServerTick")
        add_int("SkillId")
        add_short("SkillLevel")
        add_int("Count")
        add_bool("Enabled")

def decode_additional_effect2():
    with Node("additionalEffect2", True):
        add_long("additionalEffect2")

def decode_guild_invite_info():  # CGuildInviteInfo
    with Node("GuildInviteInfo", True):
        add_long("GuildUid")
        add_unicode_str("GuildName")
        add_unicode_str("UnknownStr")
        add_unicode_str("LeaderName")
        add_unicode_str("RequesterName")

def decode_guild_rank():
    with Node("GuildRank"):
        add_byte("Index")
        add_unicode_str("Name")
        add_int("PermissionFlags")

def decode_interface_text(): # sub_641140
    with Node("StringInterface"):
        b = add_bool("Unknown")
        add_int("Unknown")
        if b:
            add_int("Unknown")
            count = add_int("count")
            for i in range(count):
                add_unicode_str("UnknownStr")
        else:
            add_unicode_str("message")