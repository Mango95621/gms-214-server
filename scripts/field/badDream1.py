# id 913051000 (Ereve : Conference Room of the Alliance), field 913051000
sm.lockInGameUI(True, True)
sm.sendDelay(2000)
sm.setSpeakerType(3)
sm.setSpeakerID(1105001) # Athena Pierce
sm.setParam(1)
sm.sendNext("我们马上开始吧。")
sm.setSpeakerID(1105002) # Claudine
sm.sendSay("这要花太长时间了。而且很多人没来。你为什么喜欢独自一人？")
sm.setSpeakerID(1105003) # Neinheart
sm.sendSay("每个人都有他们的任务。克劳迪娜，要把枫之世界的所有战士聚集在一起并不容易。")
sm.setSpeakerID(1105002) # Claudine
sm.sendSay("奈因哈特爵士，执行不可能的任务是我们的职责。否则联盟还有什么存在的意义？")
sm.setSpeakerID(1105003) # Neinheart
sm.sendSay("你说话不经思考。我们为这个联盟付出了很多努力。难道大家不是都发誓要联合起来打败黑魔法师吗？")
sm.setSpeakerID(1105002) # Claudine
sm.sendSay("等等...我是在听皇家骑士团讲关于承诺的课吗？")
sm.setSpeakerID(1105001) # Athena Pierce
sm.sendSay("停止这种无谓的争论。")
sm.setSpeakerID(1105000) # Cygnus
sm.sendSay("这威胁到联盟的未来...我们承受不起公众失去信心的后果")
sm.sendSay("我们今天聚集在这里是为了讨论枫之世界发生的重大事件。")
sm.lockInGameUI(False, True)
sm.warp(913051001)
