# Bookshelf (9310600)  |  Hidden Street : Secret Library

BOOK_OF_DEMONS = 4034637
WISE_CHIEF_PRIEST = 9310053
GOBLIN_DEMON = 9310578
BLUE_DEMON = 9310577
NINE_TAILED_FOX = 9310579

if not sm.hasItem(BOOK_OF_DEMONS):
    sm.removeEscapeButton()
    sm.setBoxChat()
    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    if not sm.canHold(BOOK_OF_DEMONS):
        sm.sendNext("让我们清出一格背包空间。。我看到书就在那里。")
        sm.dispose()
    sm.sendNext("咦？这是#r恶魔之书#k")

    sm.giveItem(BOOK_OF_DEMONS)
    sm.warpInstanceIn(701220350) # hidden library

    sm.lockInGameUI(True, False)

    sm.sendNext("找到了！这一定是#p"+ str(WISE_CHIEF_PRIEST) +"#需要的那本书。我最好快去给他。")

    sm.setSpeakerID(NINE_TAILED_FOX)
    sm.setBoxChat()
    sm.sendNext("等等，#b#h0##k！我有礼物要给你！")

    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.sendNext("你为什么拿着镜子？是给我的吗？")

    sm.setSpeakerID(NINE_TAILED_FOX)
    sm.setBoxChat()
    sm.sendNext("这不是普通的镜子。\r\n"
                "它能显示一个人的真实形态，人类或恶魔。\r\n"
                "也许有一天你会觉得它有用。")

    sm.flipBoxChat()
    sm.flipBoxChatPlayerAsSpeaker()
    sm.sendNext("太棒了！谢谢！现在我得赶紧把这本书送给#p"+ str(WISE_CHIEF_PRIEST) +"#了。")

    sm.warpInstanceOut(701220300, 2) # Sutra 5-6
    sm.lockInGameUI(False)
