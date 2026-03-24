sm.setSpeakerID(9000095) # Witchy Woman
sm.sendNext("你想测试一下你的知识吗？")

response = sm.sendAskYesNo("那我们开始吧")

if response == 1:
    sm.setHintText("这是提示")
    sm.setAnswer("是")
else:
    sm.sendNext("好吧")
sm.dispose()
