BELLE = 2159314
ELEX = 2159312
BRIGHTON = 2159313
CLAUDINE = 2159315
J_AGENT = 2159344
BLACK_JACK = 2159345
CHECKY = 2159316
FERDI = 2159311

sm.lockInGameUI(True)
sm.curNodeEventEnd(True)

sm.removeEscapeButton()
sm.setSpeakerID(BELLE)
sm.sendNext("你...你真的有翅膀。")

sm.setSpeakerID(ELEX)
sm.sendSay("你是谁？是黑翼派你来做间谍的吗？实际上，这说不通...")

sm.setSpeakerID(BRIGHTON)
sm.sendSay("保持警惕。我们还不知道发生了什么。")

sm.setSpeakerID(CLAUDINE)
sm.sendSay("你是谁？你和黑翼是什么关系？")

sm.setPlayerAsSpeaker()
sm.sendSay("我完全不知道这些黑翼是什么。我从未听说过他们。你想了解我什么？我...甚至不知道从哪里开始...")

sm.setSpeakerID(J_AGENT)
sm.sendSay("好吧，让我们从你的名字、你的组织、你的背景开始...如果你不介意的话，我想知道你背上的那些翅膀。")

sm.setPlayerAsSpeaker()
sm.sendSay("我的名字是#h0#。我现在不属于任何组织...虽然我曾经是黑魔法师的指挥官之一。我反抗了他，我们战斗了，但他打败了我。当我醒来时，我看到了戴帽子的人描述的情况。哦，我天生就有这些翅膀。我的父亲是个恶魔。")

sm.setSpeakerID(CLAUDINE)
sm.sendSay("等等，等等，等等。你曾经是黑魔法师手下的指挥官？怎么可能？他已经被封印了几百年了？")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 2000)
sm.sendDelay(600)

sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, -90, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, 210, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, 100, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, -180, -100)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, -260, -50)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg0/10", 1500, 270, -50)
sm.sendDelay(1500)

sm.setSpeakerID(BELLE)
sm.sendNext("听起来像是有人脑子不太正常。实验有时会这样。有个实验对象以为自己是一把小提琴。")

sm.setPlayerAsSpeaker()
sm.sendSay("(几百年前？他们在说什么？但是...这个地方太奇怪了。我睡了多久？还有...难道是英雄们封印了黑魔法师？)")

sm.setSpeakerID(BELLE)
sm.sendSay("这说不通。你怎么看，#p2159345#？")

sm.setSpeakerID(BLACK_JACK)
sm.sendSay("这不是谎言。但这并不意味着我们的客人不是疯了。")

sm.setSpeakerID(CHECKY)
sm.sendSay("我同意Black Jack的看法。要么我们的客人疯了...要么这一切都是真的。")

sm.setSpeakerID(CLAUDINE)
sm.sendSay("如果这是真的，那么我们的客人来自几百年前，在黑魔法师被封印之前。等等，如果你是指挥官，为什么要反抗？")

sm.setPlayerAsSpeaker()
sm.sendSay("那是私人问题。现在，既然我回答了你的问题，你也回答我的。你们是谁？黑翼又是什么？")

sm.setSpeakerID(J_AGENT)
sm.sendSay("就像我之前说的，我们是反抗军。我们是一个秘密组建的组织，目的是保护我们的家园埃德尔斯坦城免受黑翼的侵害。")
sm.sendSay("那些把你当电池用的讨厌家伙就是黑翼。他们不久前入侵了埃德尔斯坦，一直在从城市中吸取能量。我们不知道原因，但我们知道他们是为黑魔法师工作的。")

sm.setPlayerAsSpeaker()
sm.sendSay("他们追随黑魔法师？我以为你说他被封印了。")

sm.setSpeakerID(ELEX)
sm.sendSay("他是被封印了。我们认为他们正在想办法再次释放他。而且，公平地说，最近有很多事件暗示这可能会发生。")

sm.setPlayerAsSpeaker()
sm.sendSay("黑魔法师要回来了？这真是好消息...")
sm.sendSay("这意味着我还能复仇！")

sm.setSpeakerID(BRIGHTON)
sm.sendSay("好吧...你有点疯狂，但我能看出我们在同一战线。")

sm.startQuest(23279)
sm.setSpeakerID(FERDI)
sm.sendSay("如果你想向黑魔法师复仇，为什么不加入我们？")

sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, -90, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, 210, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, 100, -150)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, -180, -100)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, -260, -50)
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1500, 270, -50)

sm.setSpeakerID(CLAUDINE)
sm.sendSay("校长，你在说什么...？")

sm.setSpeakerID(BRIGHTON)
sm.sendSay("你疯了吗？这明显是个陷阱！即使不是，我们要是相信黑魔法师的指挥官就是傻瓜！")

sm.setSpeakerID(FERDI)
sm.sendSay("嗯...我很高兴看到大家在这个问题上团结一致！哈！")
sm.sendSay("我相信#p2159345#的判断，而且，我们需要所有能得到的帮助。即使我们的新朋友#b曾经是#k指挥官，现在显然已经不是了。")

sm.setSpeakerID(ELEX)
sm.sendSay("而且，让指挥官和我们在一起总比和黑翼在一起好。")

sm.setSpeakerID(FERDI)
sm.sendSay("我们总是需要更多成员。只要我们的目标一致，我们就可以合作。")

sm.setPlayerAsSpeaker()
sm.sendSay("等-等等，发生了什么？我还在努力跟上这里的故事！")

sm.setSpeakerID(BELLE)
sm.sendSay("没必要跟上。决定已经做出了。如果你想对抗黑魔法师，你就必须面对黑翼，你离开这个地方的那一刻就会遇到他们。我们有共同的敌人。让我们一起合作打倒他们！")

sm.setSpeakerID(CHECKY)
sm.sendSay("谨慎是好的。我不指望你现在就完全信任我们。我们可以在逐步瓦解黑翼的过程中建立信任。")

sm.setPlayerAsSpeaker()
sm.sendSay("确实...好吧。我暂时加入你们。")
sm.sendSay("我知道这有点迟了，但是...请允许我感谢你们救了我。")

sm.setSpeakerID(J_AGENT)
sm.sendSay("非常欢迎。听到这个让我松了一口气...我从未被感谢过我的人背叛过。")

sm.setPlayerAsSpeaker()
sm.sendSay("我对忠诚于我的人忠诚。")

sm.setSpeakerID(FERDI)
sm.sendSay("对我来说没问题。好吧，请随意。我们的秘密基地就是你的秘密基地，诸如此类。")

sm.createQuestWithQRValue(23209, "1", False)
sm.completeQuest(23279)
sm.deleteQuest(23279)
sm.lockInGameUI(False)
sm.warpInstanceIn(931050040, 0)