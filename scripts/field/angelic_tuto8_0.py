# Created by MechAviv
# Map ID :: 940011080
# Western Region of Pantheon : Heliseum Hideout

sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("哇啊啊...为什么...没有...任何...事情...对我有用？！！")
sm.reservedEffect("Effect/Direction10.img/angelicTuto/Scene1")


sm.sendDelay(900)

OBJECT_1 = sm.sendNpcController(3000140, -400, 0)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
sm.sendDelay(30)


sm.moveNpcByObjectId(OBJECT_1, False, 170, 100)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(690)


sm.forcedInput(1)
sm.sendDelay(210)


sm.forcedInput(0)
sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("哦，凯尔！*抽泣* 我-我听说你现在是某种超级英雄了...那很棒。对你来说很棒。*抽泣*")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#，我一直在找你。你-你还好吗？")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我？你为什么想见我？是因为我手臂上的这个东西吗？我不是故意让它粘在那里的，但它就是...")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我早该知道会有不好的事情发生在我身上...")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#...")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我...我只是以为也许我终于能像你们一样使用魔法了。结果，我得到了一个又大又蠢的粉色手镯，还有一大堆人生我的气...我当初真不该跟你们一起来。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#，我...我的意思是，我和维德罗斯都很担心你。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("对不起。我很抱歉你们俩总是要担心我。我就待在这里，这样你们就再也不用担心我了。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("你应该继续前进，好吗？我需要一些独处的时间。")


sm.forcedInput(1)
sm.curNodeEventEnd(True)
