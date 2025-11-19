# id 913051002 (Hidden Street : Present Henesys), field 913051002
sm.lockInGameUI(True, True)
sm.hideUser(True)
sm.showFieldEffect("twilightPerion/text1", 0)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setSpeakerID(2142900) # Chief Stan
sm.setParam(1)
sm.sendNext("这很奇怪。一个镇上的所有人都做了同一个梦？")
sm.setSpeakerID(2142901) # Mrs. Ming Ming
sm.sendSay("那是个可怕的梦。光是想到它就让我脊背发凉。")
sm.setSpeakerID(2142904) # Pia
sm.sendSay("我从没想过皇家骑士团会站在黑暗势力一边...")
sm.setSpeakerID(2142902) # Bruce
sm.sendSay("我们不能确定那就是事实！")
sm.setSpeakerID(2142903) # Camila
sm.sendSay("但它太真实了，不能称之为梦。就像是通过别人的眼睛看世界一样。")
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(913051003)
