ARKARIUM = 2159309
ARK_CHAT = 2159308

sm.completeQuestNoRewards(23203)
sm.deleteQuest(23203)

sm.spawnNpc(ARKARIUM, 500, 50)
sm.showNpcSpecialActionByTemplateId(ARKARIUM, "summon", 0)
sm.lockInGameUI(True)
sm.curNodeEventEnd(True)
sm.forcedInput(2)
sm.sendDelay(30)

sm.forcedInput(0)
sm.removeEscapeButton()
sm.setSpeakerID(ARK_CHAT)
sm.sendNext("你相当强大，不是吗？我想是时候决定我们谁更强了。我一直想用我的魔法来测试你的恶魔之怒。当然，我知道谁会获胜！")

sm.chatScript("Press the Control key rapidly to block Arkarium's attack and counterattack.")
sm.showEffectOnPosition("Effect/Direction6.img/effect/tuto/guide1/0", 5010, 150, -300)
sm.showNpcSpecialActionByTemplateId(ARKARIUM, "alert", 0)
sm.showEffect("Effect/Direction6.img/effect/tuto/arkyrimAttack", 0, 0, -7, 0, sm.getNpcObjectIdByTemplateId(ARKARIUM), False, 0)
sm.sendDelay(2010)

sm.playSound("demonSlayer/arkAttack0", 100)
sm.patternInputRequest("17#17#17#", 4, 2, 3000)

sm.fadeInOut(600, 1500, 600, 150)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/9", 2000)
sm.forcedAction(376, 0)
sm.showEffect("Skill/3112.img/skill/31121000/effect", 0, 389, 83, 0, 0, True, 0)
sm.playSound("demonSlayer/31121000", 100)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/9", 2000)
sm.sendDelay(900)

sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/4", 1000, ARKARIUM)
sm.playSound("demonSlayer/31121000", 100)
sm.showNpcSpecialActionByTemplateId(ARKARIUM, "teleportation", 0)
sm.sendDelay(570)

sm.removeNpc(ARKARIUM)
sm.spawnNpc(ARKARIUM, 620, 50)
sm.showNpcSpecialActionByTemplateId(ARKARIUM, "summon", 0)
sm.sendDelay(1000)

sm.removeEscapeButton()
sm.setSpeakerID(ARKARIUM)
sm.sendNext("你比我想象的还要强大！多么有趣！")

sm.showNpcSpecialActionByTemplateId(ARKARIUM, "resolve", 0)
sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg1/10", 2000, ARKARIUM)
sm.sendDelay(1500)

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg1/11", 2000)
sm.sendDelay(1500)

sm.showEffect("Skill/3112.img/skill/31121005/effect", 0, 389, 71, 1, 0, False, 1)
sm.showEffect("Skill/3112.img/skill/31121005/effect0", 0, 389, 71, -1, 0, False, 1)
sm.playSound("demonSlayer/31121005", 100)
sm.forcedAction(370, 0)
sm.sendDelay(1980)

sm.showEffect("Effect/Direction6.img/effect/tuto/gateOpen/0", 2100, 918, -195, 0, 0, True, 0)
sm.showEffect("Effect/Direction6.img/effect/tuto/gateLight/0", 2100, 926, -390, 0, 0, True, 0)
sm.showEffect("Effect/Direction6.img/effect/tuto/gateStair/0", 2100, 879, 30, 1, 0, True, 0)
sm.playSound("demonSlayer/openGate", 100)
sm.sendDelay(1950)

sm.startQuestNoCheck(23203)
sm.showBalloonMsgOnNpc("Effect/Direction6.img/effect/tuto/balloonMsg0/0", 2000, ARKARIUM)
sm.sendDelay(1200)

sm.setSpeakerID(ARK_CHAT)
sm.sendNext("啊！看来黑魔法师终究还是想见你。很遗憾我们不能完成我们的小比赛，但一如既往，我听从我的主人。我想我会去拜访那些所谓的'英雄们'...")
sm.sendSay("至于你，#h0#，我不指望能再见到你了。好好享受黑魔法师本人赐予你的湮灭吧！哈哈哈！")

sm.showNpcSpecialActionByTemplateId(ARKARIUM, "teleportation", 0)
sm.sendDelay(570)

sm.removeNpc(ARKARIUM)
sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg2/2", 2000)
sm.forcedInput(2)