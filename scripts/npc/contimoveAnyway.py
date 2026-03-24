MAPS = [
    ["维多利亚岛站", 104020100],
    ["圣地天空渡轮", 130000210],
    ["天空之城站", 200000100],
    ["玩具城站", 220000100],
    ["阿里安特站", 260000100],
    ["神木村站", 240000100],
    ["#r埃德尔斯坦#k", 310000010]
]

text = "欢迎登船。请告诉我你想去哪里。 #b\r\n\r\n"
i = 0
while i < len(MAPS):
    text += "\r\n#L" + str(i) + "#" + str(MAPS[i][0]) + "#l"
    i += 1

answer = sm.sendNext(text)

if sm.sendAskYesNo("你想直接前往 " + str(MAPS[answer][0]) + " 吗？"):
    sm.createQuestWithQRValue(25010, str(MAPS[answer][1]))
    sm.warp(150000001, 0)
    sm.dispose()
else:
    sm.sendNext("啊，所以你想去别的地方。请告诉我你的目的地。")
    sm.dispose()
