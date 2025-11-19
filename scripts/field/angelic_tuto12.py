# Created by MechAviv
# Map ID :: 940011150
# Eastern Region of Pantheon : East Sanctum

# [SET_DRESS_CHANGED] [01 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(1)
sm.sendDelay(60)
# Unhandled User Effect [ResetOnStateForOnOffSkill] Packet: 33


sm.forcedInput(0)
sm.sendDelay(300)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg1/4", 900, 0, -120, -2, -2, False, 0)
sm.sendDelay(150)


sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(2)
sm.sendDelay(90)


sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(0)
sm.sendDelay(510)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg1/9", 900, 0, -120, -2, -2, False, 0)
sm.sendDelay(900)


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("哇哈哈哈，这就是力量吗？！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("太好玩了！全都是砰砰砰轰隆隆！！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("呃，是的。是有点像那样，只是没那么蠢。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("嘿嘿嘿，哈哈哈，哈哈哈哈哈哈！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你根本没听我说的话，对吧？嘿！别笑得那么可怕了。你需要一些练习才能正确使用我的力量。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("啊啊啊，练习？我不想练啦....")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我的力量需要变身才能真正发挥效果。我觉得你应该试试看。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("哦，好吧！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("嘿嘿嘿...咳咳，那么深入你的内心，感受我的存在，然后大声喊出来...变身！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("变身？")


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.warp(940012020, 0)
