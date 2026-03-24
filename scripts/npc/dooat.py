# Guon (2094000) | Spiegelmann's Guest House

from net.swordie.ms.constants import CustomConstants
from net.swordie.ms.enums import EventType

runsPerDay = 3

if sm.isPartyLeader():
    if sm.partyHasCoolDown(EventType.Pyramid_PQ, runsPerDay):
        sm.sendNext("你的队伍成员中有人有这个组队任务的冷却时间。")
        sm.dispose()

    sm.sendNext("你愿意帮助保卫内特金字塔吗？#b\r\n"
                "\r\n"
                "#L0#进入内特金字塔组队任务。#l")
    if sm.checkParty() and sm.checkPartyLevelReq(CustomConstants.MIN_LEVEL_FOR_PQ):

        sm.warpInstanceIn(926010100, 0, True) # Pyramid PQ  First Map
        sm.addCoolDownInXDaysForParty(EventType.Pyramid_PQ, 1, 1)

else:
    sm.sendSayOkay("请让你的队伍队长来和我对话。")
