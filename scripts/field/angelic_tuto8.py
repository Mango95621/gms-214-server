# Created by MechAviv
# Map ID :: 940011080
# Western Region of Pantheon : Heliseum Hideout

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
sm.sendNext("我该怎么办？！也许我可以躲在这里，直到我老死.")


sm.sendDelay(300)


sm.forcedInput(2)
