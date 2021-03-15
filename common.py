from script_api import *

def DecodeCoordF(str):
    with Node(str + "CoordF"):
        AddFloat("X")
        AddFloat("Y")
        AddFloat("Z")

def DecodeCoordS(str):
    with Node(str + "CoordS"):
        AddShort("X")
        AddShort("Y")
        AddShort("Z")

def DecodeEquipColor():
    with Node("EquipColor"):
        AddInt("Color1")
        AddInt("Color2")
        AddInt("Color3")
        AddInt("ColorIndex")

def DecodeSkinColor():
    with Node("SkinColor"):
        AddInt("Color1")
        AddInt("Color2")

def DecodeUgcData():
    with Node("UgcData"):
        AddLong("Unknown")
        AddUnicodeString("UUID")
        AddUnicodeString("ItemName")
        AddByte("Unknown")
        AddInt("Unknown")
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("CharacterName")
        AddLong("CreationTime")
        AddUnicodeString("UGC Url")
        AddByte("Unknown")

def DecodeSyncState():
    with Node("SyncState", True):
        AddByte("Animation1")
        AddByte("Animation2")
        flag = AddByte("Flag")
        if (flag & 1) == 1: ## bit-1
            AddInt("Unknown")
            AddShort("Unknown")
        DecodeCoordS("Position")
        AddShort("Rotation")
        u = AddByte("Unknown")
        # if u < 0???
        if u > 127:
            AddFloat("Unknown")
            AddFloat("Unknown")
        DecodeCoordS("")
        AddByte("Unknown")
        AddShort("CoordS / 10")
        AddShort("CoordS / 1000")
        if (flag & 2) == 2: ## bit-2
            DecodeCoordF("Unknown")
            AddUnicodeString("UnknownStr")
        if (flag & 4) == 4: ## bit-3
            AddInt("Unknown")
            AddUnicodeString("UnknownStr")
        if (flag & 8) == 8: ## bit-4
            AddUnicodeString("AnimationString?")
        if (flag & 16) == 16: ## bit-5
            AddInt("Unknown")
            AddUnicodeString("UnknownStr")
        if (flag & 32) == 32: ## bit-6
            AddInt("Unknown")
            AddInt("Unknown")
            AddByte("Unknown")
            DecodeCoordF("Unknown")
            DecodeCoordF("Unknown")
        AddInt("Unknown")

def DecodeItem(id):
    with Node("Item: " + str(id)):
        AddInt("Amount")
        AddInt("Unknown")
        AddInt("Unknown")
        AddLong("CreationTime")
        AddLong("ExpiryTime")
        AddLong("Unknown")
        AddInt("TimesChangedAttribute")
        AddInt("RemainingUses")
        AddByte("IsLocked")
        AddLong("UnlockTime")
        AddShort("GlamorForges")
        AddBool("Unknown")
        AddInt("Unknown")
        DecodeEquipColor()
        AddInt("Unknown")
        # Item positioning
        if id / 100000 == 113:
            AddField("Cap Position", 13 * 4)
        elif id / 100000 == 102:
            AddField("Back Hair Position", 4 * 7)
            AddField("Front Hair Position", 4 * 7)
        elif id / 100000 == 104:
            AddField("Cosmetic Position", 4 * 4)
        AddByte("Unknown")
        with Node("Stats"):
            for i in range(9):
                with Node("Iteration " + str(i)):
                    count = AddShort("count")
                    for j in range(count):
                        DecodeStatOption(j)
                    count = AddShort("count")
                    for j in range(count):
                        DecodeBonusOption(j)
                    AddInt("Unknown")
        # Sub
        AddInt("Enchants")
        AddInt("EnchantExp")
        AddBool("EnchantBasedChargeExp")
        AddLong("Unknown+191")
        AddInt("Unknown+199")
        AddInt("Unknown+203")
        AddBool("CanRepackage")
        AddInt("EnchantCharges")

        with Node("general stat diff"):
            count = AddByte("Count")
            for e in range(count):
                AddInt("stat index")
                AddInt("int diff")
                AddFloat("float diff")
        # EndSub
        #Sub
        AddInt("???")
        with Node("stat diff"):
            count = AddInt("Count")
            for i in range(count):
                DecodeStatOption(j)
        with Node("bonus stat diff"):
            count = AddInt("Count")
            for i in range(count):
                DecodeBonusOption(j)
        # EndSub

        #Testing UGC
        if id == 11400608 or id == 11500523 or id == 11600035:
            with Node("UGC", True):
                DecodeUgcData()
                AddField("Unknown", 50)

        # Pet
        if id / 100000 == 600 or id / 100000 == 610 or id / 100000 == 611 or id / 100000 == 629:
            with Node("Pet", True):
                AddUnicodeString("PetName")
                AddLong("PetExp")
                AddInt("Unknown")
                AddInt("PetLevel")
                AddByte("Unknown")

        # Music Score
        if id / 100000 == 351:
            with Node("MusicScore", True):
                AddInt("MusicId")
                AddInt("Instrument")
                AddUnicodeString("ScoreTitle")
                AddUnicodeString("Author")
                AddInt("Unknown (1)")
                AddLong("AuthorCharacterId")
                AddField("Unknown", 17)

        # Badge
        if id / 1000000 == 70:
            with Node("Badge", True):
                AddByte("Unknown")
                AddByte("Unknown")
                AddUnicodeString("BadgeIdStr")
                if id == 70100000: ## PetSkinBadge
                    AddInt("PetSkinId")
                elif id == 70100001: ## Transparency
                    AddBool("Headgear")
                    AddBool("Eyewear")
                    AddBool("Top")
                    AddBool("Bottom")
                    AddBool("Cape")
                    AddBool("Earrings")
                    AddBool("Face")
                    AddBool("Gloves")
                    AddBool("Unknown")
                    AddBool("Shoes")

        AddInt("TransferFlag")
        AddByte("???")
        AddInt("remaining trades")
        AddInt("???")
        AddByte("???")
        AddByte("???")
        f = AddByte("IsBound")
        if f != 0:
            AddLong("BoundToCharId")
            AddUnicodeString("BoundToName")
        DecodeGemSockets()
        b = AddLong("PairedCharacterId")
        if b != 0:
            AddUnicodeString("PairedName")
            AddByte("Unknown")
        AddLong("???")
        AddUnicodeString("Unknown")

def DecodeStatOption(index):
    with Node("StatOption " + str(index)):
        AddShort("StatType")
        AddInt("IntegerValue")
        AddFloat("FloatValue")
    EndNode(False)

def DecodeBonusOption(index):
    with Node("BonusOption " + str(index)):
        AddShort("StatType")
        AddFloat("FloatValue")
        AddFloat("FloatValue")
    EndNode(False)

def DecodePlayer():
    with Node("PlayerInfo"):
        AddLong("AccountId")
        AddLong("CharacterId")
        AddUnicodeString("Name")
        AddByte("Gender") # 0 = male, 1 = female
        AddByte("Unknown")
        AddLong("Unknown")

        AddInt("Unknown")
        AddInt("MapId")
        AddInt("InstanceMapId") # Guess
        AddInt("MapInstanceId") # Guess
        AddShort("Level")
        AddShort("Unknown")
        AddInt("JobGroupId")
        AddInt("JobId")
        AddInt("CurrentHp")
        AddInt("MaxHp")
        AddShort("Unknown")

        AddLong("Unknown")
        AddLong("StorageAccessTime")
        AddLong("DoctorAccessTime")
        AddInt("OutsideMapId")
        DecodeCoordF("OutsidePosition")
        AddInt("GearScore")
        DecodeSkinColor()
        AddLong("CreationTime")
        with Node("Trophy"):
            for i in range(3):
                AddInt("Count")
        AddLong("GuildUid")
        AddUnicodeString("Guild")
        AddUnicodeString("Motto")
        AddUnicodeString("Profile URL")

        # CharacterListClubParser
        with Node("Clubs"):
            count = AddByte("count")
            for i in range(count):
                b = AddByte("club")
                if b == 1:
                    AddLong("clubUid")
                    AddUnicodeString("Club Name")

        AddByte("Unknown")
        with Node("LifeSkills"):
            AddInt("Fishing???")
            AddInt("Fishing")
            AddInt("Instrument")
            AddInt("Mining")
            AddInt("Foraging")
            AddInt("Ranching")
            AddInt("Farming")
            AddInt("Smithing")
            AddInt("Handicrafts")
            AddInt("Alchemy")
            AddInt("Cooking")
            AddInt("PetTaming")

        AddUnicodeString("UnknownStr")
        AddLong("BypassKeyRelated")
        AddLong("Unknown")
        AddLong("Unknown")

        with Node("countA"):
            count = AddInt("countA")
            for i in range(count):
                AddLong("Unknown")

        AddByte("Unknown")
        AddBool("Unknown")
        AddLong("Unknown")
        AddInt("Unknown")
        AddInt("Unknown")
        AddLong("UnknownTimestamp")
        AddInt("PrestigeLevel")
        AddLong("UnknownTimestamp")

        count = AddInt("countB")
        for i in range(count):
            AddLong("Unknown")
        count = AddInt("countC")
        for i in range(count):
            AddLong("Unknown")

        AddShort("Unknown")
        AddLong("Unknown")

def DecodeNpcStats():
    with Node("NpcStats"):
        c = AddByte("Stats Flag?") # 0x35
        if c == 1:
            v = AddByte("Value")
            if v == 4:
                AddLong("Unknown")
                AddLong("Unknown")
                AddLong("Unknown")
            else:
                AddInt("Unknown")
                AddInt("Unknown")
                AddInt("Unknown")
        else:
            AddLong("Unknown")
            AddInt("Unknown")
            AddLong("Unknown")
            AddInt("Unknown")
            AddLong("Unknown")
            AddInt("Unknown")

def DecodeSkillTree():
    AddInt("JobId")
    AddByte("Unknown (1)")
    AddInt("JobGroupId")
    with Node("Skills"):
        for i in range(2):
            skillType = "Active Skills" if i == 0 else "Passive Skills"
            with Node(skillType, True):
                count = AddByte("Count")
                for j in range(count):
                    StartNode("Skill " + str(j))
                    AddBool("NewlyEnabled")
                    b = AddBool("Enabled")
                    AddInt("SkillId")
                    AddInt("Skill Points")
                    AddBool("Unknown (0)")
                    EndNode(b)
    AddByte("Unknown")
    AddByte("Unknown")

def DecodeGemSockets():
    AddByte("MaxSockets")
    count = AddByte("TotalSockets")
    for i in range(count):
        isUnlocked = AddBool("unlocked socket")
        if isUnlocked:
            DecodeGemstone()

def DecodeGemstone():
    with Node("Gemstone"):
        AddInt("GemstoneItemId")
        isBound = AddBool("Bound")
        if isBound:
            AddLong("CharacterId")
            AddUnicodeString("Name")
        b = AddBool("UnknownFlag")
        if b:
            AddByte("Unknown")
            AddLong("Unknown")

def DecodeMaid():
    AddLong("MaidUid?")
    AddLong("ItemUid")
    AddLong("Timestamp")
    AddLong("Timestamp")
    AddLong("AccountId")
    AddInt("MaidId") # 50800017
    AddInt("NpcId") # 11000785
    AddBool("IsDeployed")
    AddInt("Mood")
    AddInt("Level")
    AddInt("Closeness")
    AddLong("ExpirationTimestamp")
    count2 = AddInt("count")
    for j in range(count2):
        AddLong("Unknown")
    # Diff sub
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")
    AddUnicodeString("UnknownStr")

def DecodeAdditionalEffect():
    with Node("AdditionalEffect", True):
        AddInt("StartServerTick")
        AddInt("EndServerTick")
        AddInt("SkillId")
        AddShort("SkillLevel")
        AddInt("Unknown") # 1
        AddByte("Unknown") # 1

def DecodeGuildInviteInfo():  # CGuildInviteInfo
    with Node("GuildInviteInfo", True):
        AddLong("GuildUid")
        AddUnicodeString("GuildName")
        AddUnicodeString("UnknownStr")
        AddUnicodeString("LeaderName")
        AddUnicodeString("RequesterName")

def DecodeGuildRank():
    with Node("GuildRank"):
        AddByte("Index")
        AddUnicodeString("Name")
        AddInt("PermissionFlags?")
