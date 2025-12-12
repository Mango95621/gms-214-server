J_AGENT = 2159344
CLAUDINE = 2159315
ELEX = 2159312
BELLE = 2159314

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 2000)
sm.sendDelay(1000)

sm.removeEscapeButton()
sm.setPlayerAsSpeaker()
sm.sendNext("(我听到了什么声音...)")

sm.setSpeakerID(J_AGENT)
sm.sendSay("...我本打算发现能量传导装置后就回来。那个装置就像发电厂的那个，但这个连接着一个蛋。我正在检查的时候，那个人从蛋里出来了，击败了所有黑翼成员。太疯狂了。")

sm.setSpeakerID(CLAUDINE)
sm.sendSay("你知道吗，J...如果是别人告诉我这些，我会当面嘲笑他们。但这...黑翼在做什么？这个人是谁？")

sm.setPlayerAsSpeaker()
sm.sendSay("(他们在说我吗？)")

sm.setSpeakerID(J_AGENT)
sm.sendSay("还有那些技能...我从未见过那样的技能。太强大了...我觉得我们的客人已经没力气了，但我们还是应该小心。")

sm.setSpeakerID(ELEX)
sm.sendSay("也许这是他们的实验之一？想想维塔...而且没人真正知道黑翼在矿井深处做什么，对吧？")

sm.setSpeakerID(BELLE)
sm.sendSay("那个该死的疯子盖利默...我们必须阻止他！")

sm.setSpeakerID(J_AGENT)
sm.sendSay("...等等。我去看看我们的新朋友醒了没有。")

sm.forcedInput(2)
sm.sendDelay(2000)

sm.forcedInput(1)
sm.spawnNpc(J_AGENT, -600, -20)
sm.showNpcSpecialActionByTemplateId(J_AGENT, "summon", 0)
sm.sendDelay(30)

sm.forcedInput(0)
sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 1500, J_AGENT)
sm.sendDelay(1000)

sm.sendNext("啊，你醒了。感觉怎么样？还累吗？")

sm.setPlayerAsSpeaker()
sm.sendSay("是...你救了我吗？")

sm.setSpeakerID(J_AGENT)
sm.sendSay("是的。你伤得很重...我不能把你丢给黑翼。考虑到目前的情况，我想我们是一边的。我们有很多事要谈，不如你跟我走走？")

sm.setPlayerAsSpeaker()
sm.sendSay("(审问...？还不确定...不过他们比那些黑翼成员友好多了。)好吧。")

sm.removeNpc(J_AGENT)
sm.warpInstanceIn(931050010, 0)