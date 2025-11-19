VON_LEON = 2159310
ARKARIUM = 2159308
ORCHID = 2159339

sm.lockInGameUI(True)
sm.forcedInput(1)
sm.sendDelay(30)

sm.forcedInput(0)
sm.removeEscapeButton()
sm.setSpeakerID(VON_LEON)
sm.sendNext("除了外出执行任务的指挥官外，所有指挥官都到齐了吗？很好。我们开始会议吧。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("在伟大的黑魔法师完成他的计划之前，我们一刻也不能放松！我们仍然容易受到攻击，在黑魔法师分心时必须保持警惕。现在，#h0#，我听说你发现了一些有趣的信息。")

sm.setPlayerAsSpeaker()
sm.sendSay("是的...我发现一个抵抗组织已经秘密形成，正在集结力量来对抗我们。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("抵抗？哈！这个世界上已经没有人能抵抗我们了。我甚至听到一些乌合之众称他们为#r英雄们#k。这不是很可笑吗？")

sm.setSpeakerID(ORCHID)
sm.sendSay("当然，我有点兴奋想看看他们在最后绝望中挣扎的样子。可能会带来一些有趣的战斗。当我们占领埃雷弗时，他们确实没有进行太多抵抗。或者当我消灭城堡主时也是如此。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("埃雷弗的战斗之所以轻松是因为黑魔法师的参与，而不是因为你的力量，#p2159339#。注意你的言辞。")

sm.setSpeakerID(ORCHID)
sm.sendSay("嗯...既然黑魔法师处理了一切，我就不必使用我的全部力量了。所以，就是这样。")

sm.setPlayerAsSpeaker()
sm.sendSay("莲花似乎很忙...你在这里做什么，奥奇德？你不是和莲花一起工作吗？")

sm.setSpeakerID(ORCHID)
sm.sendSay("莲花才是那个对我太忙的人！我本来要去支援我的双胞胎兄弟...你不用一直烦我这件事。你们这些人太紧张了，不管怎样。")

sm.setSpeakerID(VON_LEON)
sm.sendSay("...这次会议毫无进展...")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("你有没有注意到，当#p2159339#开口说话时，我们的会议就会停滞不前？真有趣。至于英雄们，我相信#h0#有办法对付他们。")
sm.sendSay("既然你击倒了时间女神，我相信这些可怜的'英雄们'根本不是你的对手。")

sm.setPlayerAsSpeaker()
sm.sendSay("...他们不会那么容易消灭。与大多数敌人不同，英雄们为他人而战，而不是为自己。他们很特别，因为他们选择保护世界，而不是绝望地挣扎。这使他们变得危险。我要提醒你，我只是击晕了女神。当然，是黑魔法师击败了她。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("天哪，你真是太谦虚了！这一定是你成为黑魔法师最宠爱的指挥官的原因。你真的让我们其他人相形见绌，不是吗？哎呀呀...")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 2000)
sm.sendDelay(1500)

sm.setSpeakerID(VON_LEON)
sm.sendNext("#p2159309#，我已经听够了。#h0#击晕了时间女神，为我们赢得了胜利。那才是战斗的转折点。接受这个事实吧。")

sm.sendSay("此外，你因为弄瞎女神而得到了功劳。你还想要什么，#p2159309#？")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("哦，我什么都不想要。我只是...在做观察。我们不应该继续会议吗？英雄们会被处理掉，但剩下的抵抗组织怎么办？")

sm.setSpeakerID(VON_LEON)
sm.sendSay("按照命令，他们已经被完全消灭了。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("哦，我明白了！")

sm.setSpeakerID(ORCHID)
sm.sendSay("实际上我有个问题。为什么黑魔法师改变了我们的命令？我是说，如果我们摧毁一切，那还有谁来统治...？")

sm.setPlayerAsSpeaker()
sm.sendSay("摧毁一切？黑魔法师下达了这样的命令吗？我没有收到这样的命令。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("哦，是的！我忘了。你看起来因为与女神的史诗级战斗而太累了，我甚至没有向你提到新的命令。")

sm.sendSay("你看，我们伟大的领袖黑魔法师命令我们所有人，除了你，去消灭一切。我是说，一切！")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/18", 2000)
sm.sendDelay(1500)

sm.setSpeakerID(VON_LEON)
sm.sendNext("确实。例如，我看到莱夫雷被烧成了灰烬。什么都没剩下...")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("黑魔法师告诉我们要让世界看到抵抗的代价，所以我们开始消灭涉嫌背叛的地区。我认为我们做得相当不错。")

sm.setSpeakerID(VON_LEON)
sm.sendSay("是的...只剩下几个龙族仆人了。")

sm.setPlayerAsSpeaker()
sm.sendSay("等等，等等。黑魔法师不是承诺过不会攻击南部地区吗？哪些地方被摧毁了？")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("哪些地方？哈！当然是所有地方！我们非常认真地执行了命令。为什么...有什么困扰你吗？")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg0/11", 2000)
sm.sendDelay(1500)

sm.setPlayerAsSpeaker()
sm.sendNext("...请原谅我。有件事我必须去处理。")

sm.setSpeakerID(ARKARIUM)
sm.sendSay("站住！无论黑魔法师多么宠爱你，你都要服从命令。还没有人让你离开。坐下。这是命令。")

sm.forcedInput(2)