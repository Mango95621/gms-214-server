SKIPPER = 1096000

sm.removeEscapeButton()

sm.setSpeakerID(SKIPPER)
sm.reservedEffect("Effect/Direction4.img/cannonshooter/face03")
sm.sendNext("那么，你为什么想去枫之岛呢？这些天去那里的人不多。看你的衣服，你也不是游客。")

sm.setPlayerAsSpeaker()
sm.sendSay("我要去枫之岛进行训练。之后，我会去维多利亚岛成为一名伟大的冒险家！...就是这样，对吧？")

sm.setSpeakerID(SKIPPER)
sm.sendSay("当然是这样！枫之岛是个很好的训练场所，因为那里没有危险的怪物。而且，你会遇到很多像你一样的新手交朋友。一旦你掌握了基础，维多利亚岛就是你发光发热的地方。然后，当你准备好了，外面还有一个广阔的世界等着你去探索！啊，我真羡慕你！")

sm.setPlayerAsSpeaker()
sm.sendSay("嘿嘿，我等不及了！我会努力训练，学会打败所有最强大的怪物。我一直在学习成为一名伟大的冒险家。我已经完全准备好了！")

sm.setSpeakerID(SKIPPER)
sm.sendSay("你的态度真棒！这正是帮助你成功的东西。当然，你永远无法确定未来会发生什么。只要记住，#b一切都有原因#k。")
sm.sendSay("嘿...你听到什么了吗？嗯，我刚刚有种很奇怪的感觉。我知道海洋上没有怪物，但你还是小心点比较好。")

sm.ballonMsg("你在说什么？我什么都没感觉到...")
sm.forcedInput(2)
sm.curNodeEventEnd(True)