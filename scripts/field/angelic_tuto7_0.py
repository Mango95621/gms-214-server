# Created by MechAviv
# Map ID :: 940011070
# Pantheon : Great Temple Interior

OBJECT_1 = sm.sendNpcController(3000152, 300, 10)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("#h0#，等等！")


sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(0)
sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("这个'诅咒'并不像听起来那么不祥。那个圣物从未对其他祭司产生过反应，但它却像慈母一样紧紧依附着你。")


sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("但我不想要这些！我不是故意拿走任何东西的！")


sm.forcedInput(1)
sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/6", 1200, 0, -120, 0, OBJECT_1, False, 0)
sm.curNodeEventEnd(True)
