# Puro (1200003) | Snow Island : Penguin Port

victoriaIslandPrice = 800

answer = sm.sendNext("要出发吗？ \r\n\r\n#b"
            "#L0##e主题地下城：里恩海峡#n (价格: 0 金币)\r\n"
            "#L1#维多利亚岛 (价格: "+ str(victoriaIslandPrice) +" 金币)#l")

if answer == 0:
    sm.warp(141000000, 0)
elif answer == 1:
    if sm.getMesos() < victoriaIslandPrice:
        sm.sendSayOkay("你需要更多的钱才能使用我的服务。")
    else:
        sm.deductMesos(800)
        sm.warp(104000000, 0)
