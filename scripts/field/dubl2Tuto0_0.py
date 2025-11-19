sm.lockInGameUI(False)
sm.progressMessageFont(3, 20, 20, 0, "你可以通过点击头顶有灯泡的NPC来开始任务.")
sm.blindEffect(False)

if sm.sendAskAccept("你想跳过介绍吗?"):
    sm.levelUntil(10)
    sm.jobAdvance(400)
    sm.resetAP(chr.getJob())
    sm.warp(101000000)
    sm.giveItem(1332063)
    sm.dispose()
