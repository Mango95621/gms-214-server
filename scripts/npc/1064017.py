# Vellum NPC (1064017) | Used for the Root Abyss Quest Line

VELLUM = 1064017
if sm.hasQuest(30006):
    sm.setSpeakerID(VELLUM)
    sm.sendNext("愚蠢的生物！你竟敢挑战#r他#k的意志？！")
else:
    sm.dispose()


    sm.setPlayerAsSpeaker()
    sm.sendNext("你是什么？！")

    sm.setSpeakerID(VELLUM)
    sm.sendNext("#r他#k陛下信任我担任他的封印守护者，而你竟敢玷污他的计划。 "
                "我叫#b维尔姆#k。你活着的时间足以记住它。")

    sm.setPlayerAsSpeaker()
    sm.sendNext("是你在世界之树上施加封印的吗？")

    sm.setSpeakerID(VELLUM)
    sm.sendNext("封印是#r他陛下#k的想法。我只是按他的意志行事。")

    sm.setPlayerAsSpeaker()
    sm.sendNext("你一直提到#r他#k。你是在说那个戴眼罩的恶魔吗？")

    sm.setSpeakerID(VELLUM)
    sm.sendNext("住嘴！你这脏嘴根本不配提及#r他#k的威严！")

    sm.setPlayerAsSpeaker()
    sm.sendNext("我不是来打架的。恶魔猎人是我们的盟友。为什么你不能加入我们？")

    sm.setSpeakerID(VELLUM)
    sm.sendNext("你竟敢把那个叛徒和#r他#k相提并论？我会满足你慢慢死去的愿望！")

    sm.sendNext("我只是四大守护者之一。你们没有任何机会战胜我们。 "
                "接受你毫无意义的存在，然后永远离开。")

    sm.warp(910700200, 0) # Quest Field (Colossal Root)
    sm.lockInGameUI(False)
    sm.dispose()
