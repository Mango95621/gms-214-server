map = 200090300
string = "武陵？"
if sm.getFieldID() == 250000100:
    map = 200090310
    string = "天空之城？"
response = sm.sendAskYesNo("你想去 " + (string))

if response:
    sm.warp(map, 0)
