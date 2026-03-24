if sm.getFieldID() != 910000000 and sm.sendAskYesNo("你想传送到自由市场吗？"):
    sm.setReturnField()
    sm.warp(910000000, 2)
