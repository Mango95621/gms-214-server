# Created by MechAviv
# Map ID :: 940011090
# Eastern Region of Pantheon : Near East Sanctum

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(0)
sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("真蠢。你不能只是坐在这里哭。")


sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("也许我可以把这个愚蠢的东西放回东圣殿。然后这一切都会消失！")


sm.forcedInput(2)
