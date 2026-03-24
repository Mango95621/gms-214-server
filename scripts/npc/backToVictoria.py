map = 104020000
if sm.getFieldID() != 120040000:
    map = 120040000


if sm.sendAskYesNo("你想前往 #m" + str(map) + "# 吗？"):
    sm.warp(map, 0)
