# id 913051004 (Hidden Street : Present Ereve), field 913051004
sm.lockInGameUI(True, True)
sm.hideUser(True)
sm.showFieldEffect("twilightPerion/text6", 0)
sm.sendDelay(2500)
sm.setSpeakerType(3)
sm.setSpeakerID(2142910) # Kirium
sm.setParam(1)
sm.sendNext("你也做了那个梦吗？")
sm.setSpeakerID(2142911) # Kiriwing
sm.sendSay("这很奇怪。每个人都在做噩梦。")
sm.setSpeakerID(2142912) # Kiryu
sm.sendSay("我们有希纳斯女皇在这里安抚我们的恐惧，但其他地区的人们怎么办？")
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(913051005)
