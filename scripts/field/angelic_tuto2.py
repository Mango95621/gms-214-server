# Created by MechAviv
# Map ID :: 940011020
# Eastern Region of Pantheon : Near East Sanctum

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
OBJECT_1 = sm.sendNpcController(3000140, -1400, 0)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
OBJECT_2 = sm.sendNpcController(3000104, -1650, 0)
sm.showNpcSpecialActionByObjectId(OBJECT_2, "summon", 0)
sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("今天天气真好！我想睡个午觉！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你真是个懒虫，#h0#。凯尔和我都已经成为骑士了，而你却还想睡更多觉！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("嘿，我又不像你们那样是战士！除非我奇迹般地获得超能力，否则我每天都会整天闲逛。")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我很确定你已经跟我说过这句话大概一千次了。")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("哦，对不起，我让你觉得无聊了吗？我应该祝贺你们俩获得这些花哨的新头衔吗？总有一天我会加入你们的！")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我不认为你真的需要成为骑士，#h0#。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("你在说什么？我们是赫利西姆部队！我们必须战斗！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("是啊，但你不使用魔法。你总有一天要面对现实...")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("呃，不是每个人都必须使用魔法，你知道吗？你有时候真是固执...")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我只是希望你能偶尔思考一下。不管怎样，我得回去了。")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("哦，我真希望能去...")


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/0", 1200, 0, -120, 0, OBJECT_1, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("那是什么声音？")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你在说什么？来吧，你可以在回营地的路上做白日梦，想着和#h0#亲热。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("不，出事了！我们需要去东圣殿！")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我们出发吧！赫利西姆部队，前进！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("认真的吗？你怎么可能知道东圣殿发生了什么？")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("来吧维迪！凯尔的直觉很少出错。再说了，我很无聊！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("如果我们要一直跟着凯尔那愚蠢的直觉走，你们当初为什么要让我当队长？")


sm.moveNpcByObjectId(OBJECT_1, False, 400, 100)
sm.moveNpcByObjectId(OBJECT_2, False, 400, 100)
sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(600)


sm.forcedInput(2)