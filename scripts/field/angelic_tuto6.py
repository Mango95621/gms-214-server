# Created by MechAviv
# Map ID :: 940011060
# Pantheon : Pantheon Clinic

# [SET_DRESS_CHANGED] [00 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(1)
sm.sendDelay(60)


sm.forcedInput(0)
OBJECT_1 = sm.sendNpcController(3000106, 160, 50)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
OBJECT_2 = sm.sendNpcController(3000107, 10, 50)
sm.showNpcSpecialActionByObjectId(OBJECT_2, "summon", 0)
OBJECT_3 = sm.sendNpcController(3000152, 90, 50)
sm.showNpcSpecialActionByObjectId(OBJECT_3, "summon", 0)
sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("#h0#，你终于醒了。")


sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("呃，我在哪里？")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("万神殿。你感觉怎么样？")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我的头感觉像个熟透的西瓜，但除此之外我觉得还好。")


sm.showEffect("Effect/Direction10.img/effect/story/BalloonMsg1/0", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(600)


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendNext("嗯？为什么我手臂上有个粉色的东西？")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("孩子，我希望我有更好的消息，但我担心你被东圣殿的圣物诅咒了。事实上，它已经牢牢粘在你的手臂上了。")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("什么？！我该怎么办？！怎么把它弄下来？！")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("让一个年轻、无助的女孩带着我们的圣物在四处游荡所带来的安全隐患，我并非没有注意到。")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("不要责备这个女孩，卡塔利安。如果不是凯撒和#h0#，那个圣物早就完全消失了。")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我想你是对的，一如既往。")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("哈...哈哈哈...什么？我什么都不记得了...")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("你是说圣物抓住我，在我碰到它时变成了手镯？凯撒到底是谁？到底发生了什么？！")


sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("嘿，会没事的。我们没有办法把那个圣物从你手臂上取下来，但它不会对你造成任何伤害。就当它是一个漂亮的饰品吧。")


sm.setSpeakerID(3000152)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我-我不是故意拿走的！我甚至不喜欢粉色！")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#，没有人为此责怪你。万神殿还有三个圣物。我们相当安全。")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("但-但是，我...")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#，请不要开始哭。我是个非常敏感的同情性哭泣者。")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("呃...")


sm.setSpeakerID(3000106)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("卡塔利安！")


sm.setSpeakerID(3000107)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("对不起。我对我的泪腺控制力很差。")


sm.forcedInput(1)
