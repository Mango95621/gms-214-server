#Quick move ardent and Pflame NPC

Ardentmill = 910001000

if sm.getFieldID() == Ardentmill:
    sm.sendNext("我还没有完成\r\n#b")
elif sm.sendAskYesNo("你想被传送到阿尔德恩米尔斯吗？\r\n#b"):
    sm.setReturnField()
    sm.warp(910001000)
