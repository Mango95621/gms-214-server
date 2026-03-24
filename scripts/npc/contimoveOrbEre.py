map = 200090020

response = sm.sendAskYesNo("你想去 #m" + str (map) + "m# 吗？")

if response:
    sm.warp(map, 0)
