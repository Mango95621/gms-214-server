# Created by MechAviv
# Map ID :: 940011100
# Eastern Region of Pantheon : East Sanctum

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(0)
sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("好了，龙先生，我们到了。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你看到圣物原来位置的那个戒指了吗？")


sm.forcedInput(2)