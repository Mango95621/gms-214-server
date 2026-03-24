# a pile of herbs (1043001) | Forest of Endurance : Stage 5 (910130102)
# Forest of Endurance - The Double-Rooted Reg Ginseng (Quest 2051)
# Author: Tiger

import random

rewards = [
 [4020007, 2], # 钻石矿石
 [4020008, 2], # 黑水晶矿石
 [4010006, 2], # 金矿石
 [1032013, 1]  # 红心耳环
 ]

if sm.hasQuest(2051):
    response = sm.sendAskYesNo("你确定要带走 #b双根红参#k 吗？")

    if response:
         sm.giveItem(4031032, 1) # 双根红参
         sm.warp(101000000) # 魔法密林
else:
    rand = random.choice(rewards)
    sm.giveItem(rand[0], rand[1])
    sm.warp(101000000) # 魔法密林
