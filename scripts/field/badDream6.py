# id 913051005 (Hidden Street : Recent Elluel), field 913051005
sm.lockInGameUI(True, True)
sm.hideUser(True)
sm.showFieldEffect("twilightPerion/text7", 0)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setSpeakerID(2142934) # Deet
sm.setParam(1)
sm.sendNext("对我来说总是一样的...你也是这样吗？")
sm.setSpeakerID(2142935) # Roa
sm.sendSay("晚上睡觉太可怕了。")
sm.setSpeakerID(2142936) # Moonie
sm.sendSay("别哭了。那只是个梦。")
sm.setSpeakerID(2142933) # Klas
sm.sendSay("没必要害怕。那只是个梦。")
sm.moveCamera(False, 150, -110, -210)
sm.sendDelay(6000)
sm.setSpeakerID(2142932) # Astilda
sm.sendNext("我已经活了几百年，从未见过这样的事情。")
sm.setSpeakerID(2142931) # Danika
sm.sendSay("我们也从未听说过这种事情...会不会是黑魔法师的指挥官之一？")
sm.setSpeakerID(2142930) # Philius
sm.sendSay("我们不知道敌人的计划。他们可能只是想吓唬我们，或者只是在分散我们对更重要事情的注意力...")
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(913051006)
