# a pile of flowers (1043000) | Forest of Endurance : Stage 2 (910130001)
# Forest of Endurance (Quest 2050)
# Author: Tiger

import random

rewards = [
 4020005, # 蓝宝石矿石
 4020006, # 黄玉矿石
 4020004, # 蛋白石矿石
 4020001, # 紫水晶矿石
 4020003, # 祖母绿矿石
 4020000, # 石榴石矿石
 4020002  # 海蓝宝石矿石
 ]

if sm.hasQuest(2050): # Forest of Endurance - The Pink Anthurium Quest
    response = sm.sendAskYesNo("你确定要带走 #b粉红火鹤花#k 吗？")

    if response:
         sm.giveItem(4031020, 1) # 粉红火鹤花
         sm.warp(101000000) # 魔法密林
else:
    sm.giveItem(random.choice(rewards), 2)
    sm.warp(101000000) # 魔法密林
