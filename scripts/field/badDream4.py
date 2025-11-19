# id 913051003 (Ereve : Conference Room of the Alliance), field 913051003
sm.lockInGameUI(True, True)
sm.showFieldEffect("twilightPerion/text2", 0)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setSpeakerID(1105005) # Lady Syl
sm.setParam(1)
sm.sendNext("埃雷弗被摧毁，希纳斯转向邪恶？我们不是已经证明这只是虚假的未来吗？")
sm.setSpeakerID(1105003) # Neinheart
sm.sendSay("那不是我们的未来。那只是捏造出来的。")
sm.setSpeakerID(1105002) # Claudine
sm.sendSay("这并非完全不可能...")
sm.setSpeakerID(1105014) # Mihile
sm.sendSay("你竟敢暗示我们会参与其中？！")
sm.setSpeakerID(1105006) # Belle
sm.sendSay("你打算怎么办，金发小子？")
sm.setSpeakerID(1105001) # Athena Pierce
sm.sendSay("不要打架！")
sm.setSpeakerID(1105002) # Claudine
sm.sendSay("大家都冷静下来。如果我们要解决这个问题，需要从各个方面来看待这个情况。")
sm.setParam(17)
sm.sendSay("#b(联盟成员之间达成一致还需要一些时间。)#k")
sm.setSpeakerID(1105001) # Athena Pierce
sm.setParam(1)
sm.sendSay("这很严重。那个虚假的未来正在困扰着人们的梦境。")
sm.setSpeakerID(1105004) # Grendel the Really Old
sm.sendSay("这种事情真的可能吗？即使是训练有素的魔法师，这种梦境控制也几乎是不可能的。")
sm.setSpeakerID(1105000) # Cygnus
sm.sendSay("不仅仅是射手村。这个噩梦正在像瘟疫一样蔓延。")
sm.lockInGameUI(False, True)
sm.warp(913051004)
