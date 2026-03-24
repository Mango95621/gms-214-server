import random

items = [1050004


]


if sm.sendAskYesNo("#e嘿，我是个傻蛋但我可以给你游戏里的任何 #e#b套装#n #e！"):
    question = sm.sendAskYesNo("#e你想花费 #r2000 NX#n #e换取一个随机 #b套装 吗？")
    if question:
        sm.giveItem(random.choice(items))
        sm.deductNX(-2000)
    else:
        sm.sendNext("不")
