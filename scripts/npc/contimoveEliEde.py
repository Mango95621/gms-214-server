map = 200090701

response = sm.sendAskYesNo("你想去埃德尔斯坦吗？")

if response:
    sm.warp(map, 0)
