# Created by MechAviv
# Map ID :: 940011100
# Eastern Region of Pantheon : East Sanctum

sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg2/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("就把那个戴在你的小指上。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("这会不会电到我之类的？我讨厌恶作剧...")


sm.giveAndEquip(1222001)
sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你能不能把这个愚蠢的东西戴上，这样我才能让你变得强大？！")


sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)
sm.warp(940012000, 0)
