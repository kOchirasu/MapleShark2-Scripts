''' GAME_EVENT '''
from script_api import *

def sub_45CF80():
    with Node("sub_45CF80"):
        add_int("unknown")
        add_short("unknown")
        add_int("unknown")
        add_bool("unknown")
        add_bool("unknown")
        add_bool("unknown")
        add_bool("unknown")

def decode_game_event_cli(event): # virtual call +16
    if event == "SaleChat": # GameEventSaleChat
        pass
    elif event == "SAHotTime": # GameEventSAHotTime
        add_int("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
    elif event == "PCBangSAHotTime": # GameEventPCBangSAHotTime
        pass
    elif event == "SaleBeautyShop": # GameEventSaleBeautyShop
        pass
    elif event == "UserCondition": # GameEventUserCondition
        pass
    elif event == "MesoRevival": # GameEventMesoRevival
        pass
    elif event == "ItemBuff": # GameEventItemBuffCli
        add_int("unknown")
        add_int("unknown")
    elif event == "DungeonBonusReward": # GameEventDungeonBonusReward
        add_int("unknown")
        with Node("sub_4E38A0"):
            add_int("unknown")
            add_byte("unknown")
            add_float("unknown")
            add_float("unknown")
            add_int("unknown")
            count = add_int("count")
            for _ in range(count):
                add_int("unknown")
    elif event == "FreeAirTaxi": # GameEventFreeAirTaxi
        pass
    elif event == "Ontime": # GameEventOntimeCli
        add_int("unknown")
        add_long("time related")
    elif event == "SaleEnchant": # GameEventSaleEnchant
        add_int("unknown")
        add_int("unknown")
    elif event == "QuestTag": # GameEventQuestTag
        pass
    elif event == "BlackMarketFeeDiscount": # GameEventBlackMarketFeeDiscount
        pass
    elif event == "UGCMapSaleCoupon": # GameEventUGCMapSaleCoupon
        pass
    elif event == "PremiumMarketSale": # GameEventPremiumMarketSale
        pass
    elif event == "GameMenuPopup": # GameEventGameMenuPopupCli
        add_int("unknown")
        add_short("unknown")
        add_unicode_str("unknown")
    elif event == "EventFieldPopup": # GameEventEventFieldPopupCli
        add_int("unknown")
        add_int("unknown")
    elif event == "SaleAutoFishing": # GameEventSaleAutoFishingCli
        add_int("unknown")
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "SaleAutoPlayInstrument": # GameEventSaleAutoPlayInstrumentCli
        add_int("unknown")
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "TrafficOptimizer": # GameEventTrafficOptimizerCli
        add_int("unknown")
        add_field("force_add", 28) # this wasn't seen in IDA
    elif event == "DungeonRoomShutdown": # GameEventDungeonRoomShutdown
        pass
    elif event == "DungeonOpenPeriod": # GameEventDungeonOpenPeriod
        pass
    elif event == "FieldShutdown": # GameEventFieldShutdown
        pass
    elif event == "Sale": # GameEventSale
        pass
    elif event == "SaleRemake": # GameEventSaleRemake
        add_int("unknown")
        add_int("unknown")
        add_byte("unknown")
    elif event == "SaleGemStoneUpgrade": # GameEventSaleGemStoneUpgrade
        pass
    elif event == "SaleSkillUpgrade": # GameEventSaleSkillUpgrade
        pass
    elif event == "NpcEventDrop": # GameEventNpcEventDrop
        pass
    elif event == "BlueMarble": # GameEventBlueMarble
        pass
    elif event == "SaleUGCDesign": # GameEventSaleUGCDesign
        pass
    elif event == "MeratMarketNotice": # GameEventMeratMarketNoticeCli
        add_unicode_str("unknown")
    elif event == "EpicRestart": # GameEventEpicRestart
        pass
    elif event == "LevelUpPackage": # GameEventLevelUpPackage
        pass
    elif event == "UpdateString": # GameEventUpdateStringCli
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "StampEvent": # GameEventStampEvent
        pass
    elif event == "StampEventChar": # GameEventStampEventChar
        pass
    elif event == "TimeRunEvent": # GameEventTimeRunEvent
        pass
    elif event == "MassiveConstructionEvent": # GameEventMassiveConstructionEvent
        pass
    elif event == "EnchantRate": # GameEventEnchantRate
        pass
    elif event == "RankDuel": # GameEventRankDuel
        pass
    elif event == "GuildChampionship": # GameEventGuildChampionship
        pass
    elif event == "QuestAdditionalReward": # GameEventQuestAdditionalReward
        pass
    elif event == "MiniGameReward": # GameEventMiniGameReward
        pass
    elif event == "FieldBossReward": # GameEventFieldBossReward
        pass
    elif event == "GuildPartyDungeonReward": # GameEventGuildPartyDungeonReward
        pass
    elif event == "RankDuelReward": # GameEventRankDuelReward
        pass
    elif event == "GuildSkillSale": # GameEventGuildSkillSale
        pass
    elif event == "GuildPersonalSkillSale": # GameEventGuildPersonalSkillSale
        pass
    elif event == "GuildExp": # GameEventGuildExp
        pass
    elif event == "GuildFund": # GameEventGuildFund
        pass
    elif event == "GuildCoin": # GameEventGuildCoin
        pass
    elif event == "MasteryReward": # GameEventMasteryReward
        pass
    elif event == "NpcShopPremiumItemBonusCount": # GameEventNpcShopPremiumItemBonusCount
        pass
    elif event == "MeratMarketOpenTab": # GameEventMeratMarketOpenTab
        pass
    elif event == "WorldmapIcon": # GameEventWorldmapIconCli
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "MasteryReduce": # GameEventMasteryReduce
        pass
    elif event == "NpcShopShowItem": # GameEventNpcShopShowItem
        pass
    elif event == "UGCMapContractSale": # GameEventUGCMapContractSale
        add_int("unknown")
        add_int("unknown")
    elif event == "UGCMapExtensionSale": # GameEventUGCMapExtensionSale
        add_int("unknown")
        add_int("unknown")
    elif event == "ConstructShowItem": # GameEventConstructShowItem
        pass
    elif event == "TransferItemBound": # GameEventTransferItemBound
        pass
    elif event == "SaleItemsRestricted": # GameEventSaleItemsRestricted
        pass
    elif event == "UgcMapCommendationGM": # GameEventUgcMapCommendationGM
        pass
    elif event == "MeratMarketRecommendSwap": # GameEventMeratMarketRecommendSwap
        pass
    elif event == "DeleteUrlCache": # GameEventDeleteUrlCache
        pass
    elif event == "PetMastery": # GameEventPetMastery
        pass
    elif event == "PetBattleExp": # GameEventPetBattleExp
        pass
    elif event == "PetComposeSale": # GameEventPetComposeSale
        add_int("unknown")
        add_int("unknown")
    elif event == "ItemBox": # GameEventItemBox
        pass
    elif event == "ShutdownDropId": # GameEventShutdownDropId
        pass
    elif event == "ShutdownInteractObjectId": # GameEventShutdownInteractObjectId
        pass
    elif event == "ShutdownFunctionItem": # GameEventShutdownFunctionItem
        add_int("unknown")
        count = add_int("count")
        for _ in range(count):
            add_int("unknown")
    elif event == "ShutdownUGCUpload": # GameEventShutdownUGCUpload
        pass
    elif event == "ShutdownQuest": # GameEventShutdownQuest
        pass
    elif event == "ShutdownItemTransfer": # GameEventShutdownItemTransfer
        pass
    elif event == "ShutdownCoupleEmotion": # GameEventShutdownCoupleEmotion
        pass
    elif event == "ShutdownWedding": # GameEventShutdownWedding
        pass
    elif event == "FindDungeonHelperBonus": # GameEventFindDungeonHelperBonus
        pass
    elif event == "GuildVsGameOpen": # GameEventGuildVsGameOpen
        pass
    elif event == "ChatFiltering": # GameEventChatFiltering
        pass
    elif event == "BattlePetSpawn": # GameEventBattlePetSpawn
        pass
    elif event == "IDIP": # GameEventIDIP
        pass
    elif event == "Gallery": # GameEventGallery
        pass
    elif event == "IgnoreConstructionLockEvent": # GameEventIgnoreConstructionLockEvent
        pass
    elif event == "StarShop": # GameEventStarShop
        pass
    elif event == "Snowman": # GameEventSnowmanCli
        add_int("unknown")
        with Node("sub_4E05B0"):
            pass
        add_unicode_str("unknown")
    elif event == "Rps": # GameEventRpsCli
        add_int("unknown")
        with Node("sub_4E26B0"):
            pass
    elif event == "NpcShopTalk": # GameEventNpcShopTalk
        pass
    elif event == "ShutdownItemRemakeOption": # GameEventShutdownItemRemakeOption
        pass
    elif event == "NpcShopGivePoint": # GameEventNpcShopGivePoint
        pass
    elif event == "NpcShopResetPriceSale": # GameEventNpcShopResetPriceSale
        pass
    elif event == "Reactor": # GameEventReactor
        pass
    elif event == "CustomTriggerString": # GameEventCustomTriggerStringCli
        add_int("unknown")
        with Node("sub_4DC410"):
            pass
    elif event == "TreeWatering": # GameEventTreeWatering
        pass
    elif event == "ShutdownMapleSurvival": # GameEventShutdownMapleSurvival
        pass
    elif event == "ShutdownMapleSurvivalSquad": # GameEventShutdownMapleSurvivalSquad
        pass
    elif event == "ShutdownMapleSurvivalPass": # GameEventShutdownMapleSurvivalPass
        pass
    elif event == "ShutdownSurvivalObserver": # GameEventShutdownSurvivalObserver
        pass
    elif event == "SurvivalHotField": # GameEventSurvivalHotField
        pass
    elif event == "SurvivalDoubleHotField": # GameEventSurvivalDoubleHotField
        pass
    elif event == "SurvivalHotTime": # GameEventSurvivalHotTime
        pass
    elif event == "ShutdownBillboard": # GameEventShutdownBillboard
        pass
    elif event == "ShutdownUGCBanner": # GameEventShutdownUGCBanner
        pass
    elif event == "LuckyChance": # GameEventLuckyChance
        pass
    elif event == "SurvivalBox": # GameEventSurvivalBox
        pass
    elif event == "SurvivalMonster": # GameEventSurvivalMonster
        pass
    elif event == "SurvivalPlayRewards": # GameEventSurvivalPlayRewards
        pass
    elif event == "SurvivalKillExp": # GameEventSurvivalKillExp
        pass
    elif event == "SurvivalTimeExp": # GameEventSurvivalTimeExp
        pass
    elif event == "PublicTest": # GameEventPublicTest
        pass
    elif event == "AdventureLevelBonusExpRate": # GameEventAdventureLevelBonusExpRate
        pass
    elif event == "BurningLevelup": # GameEventBurningLevelupCli
        add_int("unknown")
        with Node("sub_4E32F0"):
            pass
    elif event == "Festival": # GameEventFestival
        pass
    elif event == "FieldEffect": # GameEventFieldEffect
        pass
    elif event == "ExchangeScrollSale": # GameEventExchangeScrollSale
        add_int("unknown")
        add_int("unknown")
        count = add_int("count")
        for _ in range(count):
            add_int("unknown")
    elif event == "ItemTradeRestriction": # GameEventItemTradeRestriction
        add_int("unknown")
        add_int("unknown")
        count = add_short("count")
        for _ in range(count):
            add_unicode_str("unknown")
        count = add_short("count")
        for _ in range(count):
            add_int("unknown")
    elif event == "MapleSurvivalPassBundle": # GameEventMapleSurvivalPassBundle
        pass
    elif event == "CollectItemGroup": # GameEventCollectItemGroup
        pass
    elif event == "ShutdownDummy": # GameEventShutdownDummy
        pass
    elif event == "SalePetCrystal": # GameEventSalePetCrystal
        pass
    elif event == "ArcadeOpen": # GameEventArcadeOpen
        pass
    elif event == "BingoEvent": # GameEventBingoEvent
        pass
    elif event == "LimitedQuantity": # GameEventLimitedQuantity
        pass
    elif event == "FinishPayback": # GameEventFinishPayback
        pass
    elif event == "DungeonExtraReward": # GameEventDungeonExtraRewardCli
        add_int("unknown")
        with Node("sub_4DC1D0"):
            count = add_int("count")
            for _ in range(count):
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
                add_int("unknown")
    elif event == "SaleHousing": # GameEventSaleHousing
        pass
    elif event == "DungeonHelpBonusReward": # GameEventDungeonHelpBonusReward
        add_int("unknown")
    elif event == "DungeonEnterTimeLimit": # GameEventDungeonEnterTimeLimit
        pass
    elif event == "CoupleDance": # GameEventCoupleDanceCli
        add_int("unknown")
        with Node("sub_4E3930"):
            pass
    elif event == "CashAttend": # GameEventCashAttendCli
        add_int("unknown")
        add_long("time related")
        add_long("time related")
        add_int("unknown")
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "AttendGift": # GameEventAttendGiftCli
        add_int("unknown")
        add_long("time related")
        add_long("time related")
        add_unicode_str("unknown")
        add_str("unknown")
        add_bool("unknown")
        add_bool("unknown")
        add_byte("unknown")
        add_byte("unknown")
        count = add_int("count")
        for _ in range(count):
            sub_45CF80()
    elif event == "DTReward": # GameEventDTRewardCli
        add_int("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
        add_unicode_str("unknown")
    elif event == "LoginNotice": # GameEventLoginNotice
        add_int("unknown")
    elif event == "CharacterCountRestricted": # GameEventCharacterCountRestricted
        add_int("unknown")
        add_int("unknown")
    elif event == "OnlinePatch": # GameEventOnlinePatch
        add_int("unknown")
    elif event == "LobbyMap": # GameEventLobbyMap
        add_int("unknown")
        add_int("unknown")
    elif event == "ReturnUser": # GameEventReturnUser
        add_int("unknown")
        with Node("sub_4E0540"):
            add_int("unknown")
            add_long("unknown")
            add_long("unknown")
            count = add_int("count")
            for _ in range(count):
                add_int("unknown")
    elif event == "ShutdownNoParam": # GameEventShutdownNoParam
        add_int("unknown")
    elif event == "ShutdownDesignersMarket": # GameEventShutdownDesignersMarket
        add_int("unknown")
    elif event == "ShutdownMusicScoreMarket": # GameEventShutdownMusicScoreMarket
        add_int("unknown")
    elif event == "Shutdown": # GameEventShutdown
        add_int("unknown")
    elif event == "ShutdownShop": # GameEventShutdownShop
        add_int("unknown")
    elif event == "ShutdownDungeonMatch": # GameEventShutdownDungeonMatch
        add_int("unknown")
    elif event == "ShutdownNpcTalk": # GameEventShutdownNpcTalk
        add_int("unknown")
    elif event == "ShutdownMastery": # GameEventShutdownMastery
        add_int("unknown")
    elif event == "ShutdownMasteryReward": # GameEventShutdownMasteryReward
        add_int("unknown")
    elif event == "ShutdownEnchantScroll": # GameEventShutdownEnchantScroll
        add_int("unknown")
    elif event == "ShutdownItemSocketTarget": # GameEventShutdownItemSocketTarget
        add_int("unknown")
    elif event == "ShutdownItemSocketTargetGemStone": # GameEventShutdownItemSocketTargetGemStone
        add_int("unknown")
    elif event == "ShutdownUGCDownload": # GameEventShutdownUGCDownload
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "StringBoardLink": # GameEventStringBoardLink
        add_int("unknown")
        add_unicode_str("unknown")
    elif event == "StringBoard": # GameEventStringBoardCli
        add_int("unknown")
        add_int("unknown")
        add_unicode_str("unknown")
    else:
        add_field("NOT_FOUND")


f = add_byte("Function")
if f == 0:
    count = add_int("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            event = add_unicode_str("event")
            decode_game_event_cli(event)
elif f == 1:
    count = add_int("count")
    for i in range(count):
        event = add_unicode_str("event")
        decode_game_event_cli(event)
elif f == 2:
    count = add_int("count")
    for i in range(count):
        add_int("unknown")
elif f == 3:
    count = add_int("count")
    for i in range(count):
        with Node("Entry " + str(i)):
            event = add_unicode_str("event")
            decode_game_event_cli(event)
