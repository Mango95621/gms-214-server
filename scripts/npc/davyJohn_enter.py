# Guon (2094000) | Spiegelmann's Guest House

from net.swordie.ms.constants import CustomConstants
from net.swordie.ms.constants import GameConstants
from net.swordie.ms.enums import EventType

pqItems = [
4001117, # 旧金属钥匙
4001120, # 新手海盗标志
4001121, # 崛起海盗标志
4001122, # 老兵海盗标志
]
runsPerDay = 3

if sm.isPartyLeader():
    sm.sendNext("你愿意帮助我对抗戴维·约翰吗？#b\r\n"
                "\r\n"
                "#L0#进入海盗王组队任务#l")
    if sm.partyHasCoolDown(EventType.Pirate_PQ, runsPerDay):
        sm.sendNext("你的队伍成员中有人有这个组队任务的冷却时间。")
        sm.dispose()
    if sm.checkParty() and sm.checkPartyLevelReq(CustomConstants.MIN_LEVEL_FOR_PQ):

        # check for items
        for item in pqItems:
            if sm.hasItem(item):
                quantity = sm.getQuantityOfItem(item)
                sm.consumeItem(item, quantity)

        # for each party member, create a LORD_PIRATE_QUEST with qrValue = "0"
        for partyMember in sm.getParty().getMembers():
            sm.createQuestWithQRValue(partyMember.getChr(), GameConstants.LORD_PIRATE_QUEST, "0", False)

        sm.addCoolDownInXDaysForParty(EventType.Pirate_PQ, 1, 1)
        sm.warpInstanceIn(925100000, 0, True) # Lord Pirate PQ  First Map

else:
    sm.sendSayOkay("请让你的队伍队长来和我对话。")
