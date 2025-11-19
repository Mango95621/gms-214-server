SNIFFS = 3002003

sm.setSpeakerID(2007)
if sm.sendAskYesNo("是否跳过教程过场动画？"):
    sm.createQuestWithQRValue(37999, "SKIP_RAIN_EXPLAIN")
if sm.getQRValue(37999) != "SKIP_RAIN_EXPLAIN":
    sm.lockInGameUI(True, False)
    sm.hideUser(False)
    sm.spawnNpc(SNIFFS, -512, 5)
    sm.showNpcSpecialActionByTemplateId(SNIFFS, "summon")
    sm.sendDelay(1000)

    sm.removeEscapeButton()
    sm.setSpeakerID(SNIFFS)
    sm.sendNext("影！有不好的事情发生了！")

    sm.forcedInput(1)
    sm.sendDelay(100)

    sm.forcedInput(0)
    sm.setPlayerAsSpeaker()
    sm.sendNext("...嗯，我的情况也不是很好...总之，发生了什么？")

    sm.setSpeakerID(SNIFFS)
    sm.sendSay("镇-镇上下雨了！")

    sm.setPlayerAsSpeaker()
    sm.sendSay("下雨？嗯，我想这是我第一次在这个小镇看到下雨。但为什么这么糟糕？房子有损坏吗？")

    sm.setSpeakerID(SNIFFS)
    sm.sendSay("不，不！下雨意味着...意味着...你应该听族长亲口说。快点，去和他谈谈！")

    sm.removeNpc(SNIFFS)
sm.startQuestNoCheck(38019)
sm.startQuestNoCheck(38903)  # interestingly enough if you do the skip in GMS it doesn't start raining so this quest isn't started
sm.lockInGameUI(False)
sm.warp(410000001, 0)
