# Alicia's Soul | Tower of Oz (992000000)

from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

#######################################
    # THIS IS TEMPORARY UNTIL OZ IS CODED #
    #######################################

# Mode, Required Level, Map ID, Death Count, Event Type

destinations = [
    ["普通", 120, 992050000, 20, EventType.Dorothy],
]

runsPerDay = 1

if sm.getFieldID() == 992000000:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.sendAskYesNo

    dialog = "你想前往'#b海底50层#k'挑战 \r\n#b多萝西#k 吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往海底50层 (%s 模式) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#算了。"
    response = sm.sendSay(dialog)

    if not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战 #b多萝西#k 的话。")

    if sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        sm.sendNext("你或你的队伍成员在过去24小时内已经尝试挑战过 \r\n#b多萝西#k 了。")
        sm.dispose()

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.DOROTHY_TIME)
            sm.addCoolDownInXDaysForParty(destinations[response][4], 1, 1)
        else:
            sm.sendSayOkay("一个或多个队伍成员缺少前置任务，或等级低于 #b%d#k。" % destinations[response][1])
