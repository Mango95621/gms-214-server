# Created by MechAviv
# Map ID :: 940011030
# Eastern Region of Pantheon : East Sanctum

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(30)


sm.forcedInput(0)
OBJECT_1 = sm.sendNpcController(3000140, -300, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
OBJECT_2 = sm.sendNpcController(3000104, -450, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_2, "summon", 0)
OBJECT_3 = sm.sendNpcController(3000110, -120, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_3, "summon", 0)
OBJECT_4 = sm.sendNpcController(3000114, -50, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_4, "summon", 0)
OBJECT_5 = sm.sendNpcController(3000111, 130, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_5, "summon", 0)
OBJECT_6 = sm.sendNpcController(3000115, 250, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_6, "summon", 0)
sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("这里什么都没有，真是意料之中...")


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/0", 1200, 0, -120, 0, OBJECT_2, False, 0)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/0", 1200, 0, -120, 0, OBJECT_1, False, 0)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/3", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("嘿，那些祭司是谁？我以前从没见过他们。")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("维尔德罗斯，这不对劲！")


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你说得对。他们看起来很可疑。我要跑回基地寻求帮助。你们两个留在这里盯着他们，好吗？但别逞英雄。如果他们发现你们，就赶紧离开这里。")


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg0/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(900)


sm.setSpeakerID(3000104)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("他们在谈论什么？")


sm.sendNpcController(OBJECT_2, False)
sm.setSpeakerID(3000110)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("圣物的消失应该会削弱防护罩。")


sm.setSpeakerID(3000114)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我以为圣物被诅咒了...我们真的应该碰它吗？")


sm.setSpeakerID(3000110)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我没想到他们竟然允许迷信的傻瓜加入我们的教团！你会对命运的召唤退缩吗？")


sm.setSpeakerID(3000110)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("(他们是想偷走圣物吗？)")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("他们要把圣物拿走了！")


sm.setSpeakerID(3000140)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我们去阻止他们！")


sm.moveNpcByObjectId(OBJECT_1, False, 300, 100)
sm.sendDelay(300)


sm.forcedInput(2)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, OBJECT_3, False, 0)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, OBJECT_4, False, 0)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, OBJECT_5, False, 0)
sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/1", 1200, 0, -120, 0, OBJECT_6, False, 0)
sm.sendDelay(300)


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/6", 900, 0, -120, -2, -2, False, 0)
sm.sendDelay(300)


sm.showFieldEffect("kaiser/tear_rush", 0)
