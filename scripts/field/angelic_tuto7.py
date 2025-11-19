# Created by MechAviv
# Map ID :: 940011070
# Pantheon : Great Temple Interior

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(0)
sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("我偷了东西! 我从来没有偷过任何东西。我发誓，我不是故意的!")


sm.setSpeakerID(0)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我甚至没有魔法值……我什么都做不了。..我没用.... ")


sm.forcedInput(1)
sm.sendDelay(120)


sm.reservedEffect("Effect/Direction10.img/angelicTuto/Scene1")
sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/5", 1200, 0, -120, -2, -2, False, 0)
