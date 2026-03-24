sm.setSpeakerID(9400534) # Goddess Avaracia
sm.sendNext("你准备好开始了吗？")

sm.setPlayerAsSpeaker() # Player
sm.sendNext("你在说什么？你是谁？")

sm.setSpeakerID(9400534) # Goddess Avaracia
response = sm.sendAskYesNo("没有多少时间解释了，你会帮我吗？")

if response == 1:
    sm.sendNext("请去消灭100个 #r#o9390010##k，它们必须被处理掉。")
    sm.startQuest(14524)
else:
    sm.sendSayOkay("我猜你无法胜任这个任务")
sm.dispose()
