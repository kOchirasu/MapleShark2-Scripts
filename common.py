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

def decode_skin_color():
    with Node("SkinColor"):
        add_int("Color1")
        add_int("Color2")

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

def decode_player():
    with Node("PlayerInfo"):
        add_long("AccountId")
        add_long("CharacterId")
        add_unicode_str("Name")
        add_byte("Gender") # 0 = male, 1 = female
        add_byte("Player+78")
        add_long("Player+18")

        add_int("Player+20")
        add_int("MapId")
        add_int("InstanceMapId") # Guess
        add_int("MapInstanceId") # Guess
        add_short("Level")
        add_short("ChannelId")
        add_int("JobCode")
        add_int("JobId")
        add_int("CurrentHp")
        add_int("MaxHp")
        add_short("Player+4C")
        add_long("Player+50")
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

        add_byte("Player+24") # PCBang something
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

        add_byte("Player+178") # Mentor something
        add_bool("Player+17C")
        add_long("Birthday")
        add_int("Player+188") # SuperWorldChat something
        add_int("Player+18C") # Pet something
        add_long("TimestampNow?")
        add_int("PrestigeLevel")
        add_long("LoginTimestamp?")

        # these are both related?
        count = add_int("countB")
        for i in range(count):
            add_long("Player+1B0")
        count = add_int("countC")
        for i in range(count):
            add_long("Player_1C8")

        add_short("Player+1A0") # Survival something
        add_long("Player+88")

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
