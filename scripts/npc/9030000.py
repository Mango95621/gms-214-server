# Fredrick and quick move NPC

Freemarket = 910000000

if sm.getFieldID() == Freemarket:
    sm.getItemsFromTrunkEmployee()
elif sm.sendAskYesNo("你想被传送到自由市场吗？\r\n#b"):
    sm.setReturnField()
    sm.warp(910000000)