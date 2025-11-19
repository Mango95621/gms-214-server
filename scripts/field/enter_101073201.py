# id 101073201 (Mandraky Field : Kidnapping Site), field 101073201
sm.lockInGameUI(True, True)
sm.hideUser(True)
sm.spawnNpc(1500026, -322, 228)
sm.showNpcSpecialActionByTemplateId(1500026, "summon", 0)
sm.spawnNpc(1500031, 40, 228)
sm.showNpcSpecialActionByTemplateId(1500031, "summon", 0)
sm.spawnNpc(1500032, 180, 228)
sm.showNpcSpecialActionByTemplateId(1500032, "summon", 0)
sm.setSpeakerType(3)
sm.setSpeakerID(1500016) # Woonie the Fairy
sm.setParam(1)
sm.sendNext("我好害怕...我们只是在排练我们的戏剧...")
sm.setSpeakerID(1500018) # Tracy the Fairy
sm.sendSay("别担心，Woonie。一切都会好起来的！会有人来救我们的...我想...")
sm.setSpeakerID(1500026) # ???
sm.sendSay("这是什么？鼹鼠王领地上的小精灵女士们？！你们一定是多么勇敢的小点心啊！")
sm.setSpeakerID(1500018) # Tracy the Fairy
sm.sendSay("请放了我们。我不想成为鼹鼠的食物！")
sm.setSpeakerID(1500026) # ???
sm.sendSay("哦，我不会吃你们的！我会把你们留作我的新娘！等你们长大了，显然，我们鼹鼠有很强的骑士精神。")
sm.setSpeakerID(1500016) # Woonie the Fairy
sm.sendSay("什么？！恶心！")
sm.setSpeakerID(1500026) # ???
sm.sendSay("如果我冒犯了您，女士，我很抱歉，但我不会在潮湿黑暗的地下度过我的日子！一旦我把所有这些曼德拉草从你们压迫性的精灵统治中解放出来，我将成为这里的统治者，而你们会爱上我...只要你们同意的话。")
sm.setSpeakerID(1500018) # Tracy the Fairy
sm.sendSay("好吧，必须有人来救我们。")
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(101073100)
