# Hidden street : The Nightmare
sm.lockInGameUI(True)
sm.setPlayerAsSpeaker()
sm.sendNext("这一定是...哦！是女王！")
sm.forcedInput(2)
sm.sendDelay(100)
sm.sendNext("她在盯着什么看？")
#todo add wz scene for cygnus appearing in mirror
sm.warp(913031002, 0)
sm.startQuest(20893)
sm.lockInGameUI(False)


