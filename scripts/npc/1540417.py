# Quick Move Pokemon

PCcafe = 193000000

if sm.getFieldID() == PCcafe:
    sm.sendNext("我还没有完成\r\n#b")
elif sm.sendAskYesNo("你想被传送到网吧吗？\r\n#b"):
    sm.warp(193000000)
