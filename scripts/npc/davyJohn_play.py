# Guon (2094002) | Inside the  Lord Pirate Party Quest

from net.swordie.ms.constants import GameConstants
from net.swordie.ms.constants import WzConstants

pqItems = [
4001117, # 旧金属钥匙
4001120, # 新手海盗标志
4001121, # 崛起海盗标志
4001122, # 老兵海盗标志
]

ROOKIE_PIRATE_MARK = 4001120 # Stage 0
RISING_PIRATE_MARK = 4001121 # Stage 1
VETERAN_PIRATE_MARK = 4001122 # Stage 2
count = 5

stage = int(sm.getQRValue(GameConstants.LORD_PIRATE_QUEST))


if sm.getFieldID() == 925100100: # Hidden Street: Through the Head of the Ship!
    item = 0
    if stage == 0:
        item = ROOKIE_PIRATE_MARK
    elif stage == 1:
        item = RISING_PIRATE_MARK
    elif stage == 2:
        item = VETERAN_PIRATE_MARK

    nextItem = 0
    if stage == 0:
        nextItem = RISING_PIRATE_MARK
    elif stage == 1:
        nextItem = VETERAN_PIRATE_MARK

    if sm.isPartyLeader():
        if stage == 3:
            sm.sendNext("通过右边的传送门继续前进")

        else:
            if sm.hasItem(item, count):
                if stage == 2:
                    sm.sendNext("太棒了，你现在可以继续到下一阶段了！")
                    sm.invokeForParty("showEffectToField", WzConstants.EFFECT_CLEAR)

                else:
                    sm.sendNext("好的，接下来我需要 "+ str(count) +" #v"+ str(nextItem) +"##b#t"+ str(nextItem) +"##k。")
                sm.consumeItem(item, count)
                sm.invokeForParty("setQRValue", GameConstants.LORD_PIRATE_QUEST, str(int(sm.getQRValue(GameConstants.LORD_PIRATE_QUEST)) + 1))

            else:
                sm.sendNext("请给我带来 "+ str(count) +" #v"+ str(item) +"##b#t"+ str(item) +"##k。")
    else:
        sm.sendSayOkay("请让你的队伍队长来和我对话。")


elif sm.getFieldID() == 925100500: # Hidden Street: The Captain's Dignity
    if not sm.hasMobsInField():
        if not sm.isPartyLeader():
            sm.sendSayOkay("请让你的队伍队长来和我对话。")
        else:
            sm.sendNext("你帮了我们一个大忙，我们该如何报答你呢？")
        sm.warpInstanceIn(925100700, True)
        # For all party members
        for partyMembers in sm.getParty().getMembers():
            # Sets the Stage2 progress back to 0
            if partyMembers.getChr() is None:
                continue

            sm.setQRValue(partyMembers.getChr(), GameConstants.LORD_PIRATE_QUEST, "0")

            # Gives all party members Exp
            sm.giveExp(sm.getPQExp(partyMembers.getChr()))

            # Checks & deletes all items in the  array: pqItems
            for item in pqItems:
                if sm.hasItem(item):
                    quantity = sm.getQuantityOfItem(item)
                    sm.consumeItem(item, quantity)

    else:
        sm.sendSayOkay("请消灭船长！")

elif sm.getFieldID() == 925100700: #pq exist of completion
     sm.giveNX(200000)
     sm.giveItem(4310212, 2)
     sm.warpInstanceOut(910002000)
     sm.setQRValue(GameConstants.LORD_PIRATE_QUEST, "0")

else:
    response = sm.sendAskYesNo("你确定要离开吗？")
    if response:
        if not sm.getParty() is None:
            sm.warpInstanceOut(910002000)
            for partyMembers in sm.getParty().getMembers():
                sm.setQRValue(partyMembers.getChr(), GameConstants.LORD_PIRATE_QUEST, "0", True)
        else:
            sm.warpInstanceOut(910002000, 0)
            sm.setQRValue(GameConstants.LORD_PIRATE_QUEST, "0")
