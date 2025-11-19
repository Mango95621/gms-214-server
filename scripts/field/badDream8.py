# id 913051007 (Ereve : Conference Room of the Alliance), field 913051007
sm.lockInGameUI(True, True)
sm.showFieldEffect("twilightPerion/text2", 0)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setSpeakerID(1105001) # Athena Pierce
sm.setParam(1)
sm.sendNext("我们无法知道黑魔法师的梦境大师在做什么，但我们不能再让人们受苦了。")
sm.setSpeakerID(1105009) # Evan
sm.sendSay("联盟计划如何解决这个问题？")
sm.setSpeakerID(1105001) # Athena Pierce
sm.sendSay("沉默十字军已经尝试过一种解决方法...但这还不够。")
sm.sendSay("我想请你们所有人帮助我安抚勇士之村的居民，在事态失控之前。这是联盟目前的最高优先事项。")
sm.lockInGameUI(False, True)
sm.completeQuestNoCheck(31900)
sm.warp(913050010)
