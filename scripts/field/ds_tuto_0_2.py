# Dialog Constants
MASTEMA = 2159307
sm.removeEscapeButton()
sm.setSpeakerID(MASTEMA)

sm.sendNext("...你还好吗？你看起来不太一样...是的，确实不一样了。以前我问你这种事情时你都会责骂我，但现在...嘿，你看起来不太好。发生什么事了吗？你受伤了吗？")

sm.setPlayerAsSpeaker()
sm.sendSay("...告诉我，#p2151009#。你效忠于谁？是我，还是黑魔法师？")

sm.setSpeakerID(MASTEMA)
sm.sendSay("什-什么？你为什么要问我这种-")

sm.setPlayerAsSpeaker()
sm.sendSay("回答我！")

sm.setSpeakerID(MASTEMA)
sm.sendSay("嗯...呃...我当然效忠于黑魔法师...但是那天你救了我的命，我就发誓效忠于你了。你去哪里我就去哪里。呃，这，这回答了你的问题吗？")

sm.setPlayerAsSpeaker()
sm.sendSay("是的。那么我有个请求要拜托你。")
sm.sendSay("把这封信交给#r英雄们#k。")

sm.setSpeakerID(MASTEMA)
sm.sendSay("做什么？！为什么...你在想什么？发生了这么多事情之后，你还想把事情搞得更糟？如果有人发现你试图联系英雄们，你这个指挥官就完蛋了！")

sm.setPlayerAsSpeaker()
sm.sendSay("我已经不再是合格的指挥官了。")

sm.setSpeakerID(MASTEMA)
sm.sendSay("等等...你要背叛黑魔法师吗？但是，你是他最忠诚的指挥官啊！你几乎是把时间神殿拱手送给了他！我们拥有一切...你为什么要这样做？")

sm.setPlayerAsSpeaker()
sm.sendSay("没时间解释了！如果你真的效忠于我，就按我说的做。否则...")

sm.setSpeakerID(MASTEMA)
sm.sendSay("不！不...我会做的。我只是...担心你。")

sm.setPlayerAsSpeaker()
sm.sendSay("......")

sm.setSpeakerID(MASTEMA)
sm.sendSay("我是说，你的家人怎么办？他们不会有危-")

sm.setPlayerAsSpeaker()
sm.sendSay("住口！不要再提我的家人...")

sm.setSpeakerID(MASTEMA)
sm.sendSay("...什么？难...难道他们已经出事了...？")

sm.setPlayerAsSpeaker()
sm.sendSay("......")

sm.setSpeakerID(MASTEMA)
sm.sendSay("我明白了...你一直都是沉默寡言的类型，但沉默有时胜过千言万语。")
sm.sendSay("很好。我向你发誓，以我的生命起誓，我一定会把这封信送到英雄们手中。")

sm.setPlayerAsSpeaker()
sm.sendSay("谢谢你。很抱歉要你去做这种事，#p2151009#...")

sm.setSpeakerID(MASTEMA)
sm.sendSay("不用道歉。毕竟我欠你一条命。事实上，我...我真的很感激你的信任。")
sm.sendSay("好吧...我走了。无论你在做什么...祝你好运。")

sm.showNpcSpecialActionByTemplateId(MASTEMA, "teleportation", 0)
sm.sendDelay(720)

sm.removeNpc(MASTEMA)
sm.setPlayerAsSpeaker()
sm.sendNext("(你的忠诚对我来说意义重大，#p2151009#。谢谢你。)")

sm.forcedInput(2)
sm.curNodeEventEnd(True)