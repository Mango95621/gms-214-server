sm.setSpeakerType(2)
sm.setParam(546)
sm.setColor(1)
sm.setSpeakerID(9000139) # Kitty
sm.setInnerOverrideSpeakerTemplateID(9000139) # Kitty
if sm.hasQuestCompleted(14256):
    if sm.sendAskYesNo("你想去#b万圣节派对#k吗？"):
        sm.warp(993034000)
else:
    sm.sendNext("嘿！别碰我的猫，她现在非常害怕。。")
    sm.setParam(547)
    sm.sendNext("这是怎么回事")
    sm.setSpeakerType(2)
    sm.setParam(546)
    sm.setSpeakerID(9000139)
    sm.sendNext("我们被困在这里了。。有什么黑暗的东西把主门锁住了，我们不知道该怎么办。。")
    sm.setParam(547)
    sm.sendNext("好吧，也许我能帮上忙？你能让我摸一下那只猫吗？")
    sm.setParam(546)
    sm.setSpeakerID(9000139)
    if sm.sendAskYesNo("我会考虑一下。\r\n但你能帮我们逃离这个噩梦吗？"):
        sm.sendNext("谢谢你^^")
    else:
        sm.sendNext("你不必这么过分。。好吧，不能让你摸猫了。")
