GUARD1 = 2159340
GUARD2 = 2159341
J_AGENT = 2159342

sm.lockInGameUI(True)
sm.completeQuestNoRewards(23207)
sm.deleteQuest(23207)

sm.spawnNpc(GUARD1, 175, 0)
sm.showNpcSpecialActionByTemplateId(GUARD1, "summon", 0)
sm.spawnNpc(GUARD2, 300, 0)
sm.showNpcSpecialActionByTemplateId(GUARD2, "summon", 0)
sm.spawnNpc(J_AGENT, 600, 0)
sm.showNpcSpecialActionByTemplateId(J_AGENT, "summon", 0)
sm.showNpcSpecialActionByTemplateId(GUARD1, "panic", 0)
sm.showNpcSpecialActionByTemplateId(GUARD2, "panic", 0)

sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 1500, J_AGENT)
sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 1500, GUARD1)
sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/3", 1500, GUARD2)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg2/0", 1500)# for player ofc
sm.sendDelay(1500)

sm.forcedInput(0)
sm.removeEscapeButton()
sm.setSpeakerID(GUARD1)
sm.sendNext("那-那是什么？")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg2/1", 2000)
sm.sendDelay(900)

sm.setPlayerAsSpeaker()
sm.sendNext("(发生了什么？我的恶魔之怒...几乎消失了！这个东西是什么？它夺走了我的力量...？)")

sm.setSpeakerID(GUARD2)
sm.sendSay("这-这不可能发生...！")

sm.setPlayerAsSpeaker()
sm.sendSay("你们对我做了什么？这种能量...是黑魔法师的能量吗？")

sm.setSpeakerID(GUARD1)
sm.sendSay("需要抓住那个人以避免审讯...")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/16", 2000)
sm.sendDelay(1500)

sm.fadeInOut(600, 1500, 600, 150)
sm.forcedAction(372, 0)
sm.showEffect("Skill/3112.img/skill/31121006/effect", 0, 0, 0, 0, 0, False, 0)# should make method for skill effect
sm.playSound("demonSlayer/31121006", 100)
sm.reservedEffect("Effect/Direction6.img/DemonTutorial/Scene3")
sm.sendDelay(900)

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/17", 2000)
sm.sendDelay(900)

sm.playSound("demonSlayer/31121006h", 100)
sm.startQuestNoCheck(23207)
sm.showNpcSpecialActionByTemplateId(GUARD1, "die", 0)
sm.showNpcSpecialActionByTemplateId(GUARD2, "die", 0)
sm.sendDelay(990)

sm.removeNpc(GUARD1)
sm.removeNpc(GUARD2)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg0/13", 2000)

sm.setSpeakerID(J_AGENT)
sm.sendNext("(那是谁？我从未见过如此强大的技能...)")

sm.sendDelay(1500)

sm.setPlayerAsSpeaker()
sm.sendNext("(呃...我在和他们战斗时浪费了太多力量。我在哪里？无论如何，我知道我需要离开这里。)")

sm.forcedInput(2)
sm.sendDelay(990)

sm.forcedInput(0)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/12", 2000)



sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 2000, J_AGENT)
sm.sendDelay(1200)

sm.moveNpcByTemplateId(J_AGENT, True, 150, 100)

sm.sendNext("(不...我...正在失去意识。如果他们现在找到我...！)")

sm.setSpeakerID(J_AGENT)
sm.sendSay("等等，冷静下来。我不是你的敌人。你是谁？你是怎么来到这种地方的？")

sm.setPlayerAsSpeaker()
sm.sendSay("(他感觉不邪恶...)\r\n退后！")

sm.setSpeakerID(J_AGENT)
sm.sendSay("来吧...看看你自己。你需要帮助，而且现在就需要。你意识到他们在做什么吗？你旁边的那个机器是一个能量传导装置...黑翼正在吸取你的力量。")

sm.setPlayerAsSpeaker()
sm.sendSay("(能量传导装置？这个机器？黑翼是谁？这一切都没有任何意义...)")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg0/13", 2000)
sm.sendDelay(1500)

sm.sendNext("你是谁？而且...*咳嗽* 你怎么知道这些事情？")

sm.setSpeakerID(J_AGENT)
sm.sendSay("我是J，抵抗组织的特工。我们正在对抗黑翼。我不知道你是谁，但我不会在你这种状态下占你便宜。让我帮助你。")

sm.setPlayerAsSpeaker()
sm.sendSay("不...我...没有能量了...")

sm.forcedAction(379, 0)
sm.showEffect("Effect/Direction6.img/effect/tuto/fallMale", 0, 0, 0, 0, 0, False, 0)
sm.sendDelay(600)

sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/13", 2000, J_AGENT)
sm.sendDelay(1500)

sm.removeNpc(J_AGENT)
sm.warpInstanceIn(931050030, 0)