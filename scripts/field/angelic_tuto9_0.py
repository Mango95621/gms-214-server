# Created by MechAviv
# Map ID :: 940011090
# Eastern Region of Pantheon : Near East Sanctum

sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/1", 1200, 30, -70, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg0/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/2", 1200, 0, -120, -2, -2, False, 0)
sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(2)
sm.sendDelay(120)


sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(0)
sm.sendDelay(600)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/7", 1200, 30, -70, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/3", 1200, 30, -70, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg1/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(1800)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/4", 1200, 30, -70, -2, -2, False, 0)
sm.sendDelay(1200)


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg0/8", 1200, 30, -70, -2, -2, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("嘿！小姑娘。你能看见我吗？")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("什么鬼——")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("啊！放松！我是埃斯卡拉德。我，呃，我住在你柔软手腕上的那个手镯里。我在想，既然我们，嗯，连在一起了，也许我可以给你一点我的力量。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("力量？你在说什么？")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("就去你拿到那个圣物的地方。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("好吧，但我不会仅仅因为你告诉我才去。我本来就打算去那里。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("好吧！我怎么就摊上了这么个不听话的小鬼？")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("如果你这么无礼，我不会带你去任何地方。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("谁无礼了？！我是在给你终极力量，来换取你去一个你本来就打算去的地方！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("哦，是啊，我想这是真的。")


sm.forcedInput(2)
sm.curNodeEventEnd(True)
