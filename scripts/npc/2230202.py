from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type

destinations = [
    ["传奇", 250, 924045000, 20, EventType.Hekaton],
]

runsPerDay = 1

if sm.getFieldID() == 302090500:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.sendAskYesNo

    dialog = "你想前往'#bTrueffet#k'挑战 \r\n#b赫卡顿#k吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往Trueffet (%s模式) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#算了。"
    response = sm.sendSay(dialog)

    if not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战 #b赫卡顿#k 的话。")

    if sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        sm.sendNext("你或你的队伍成员在过去7天内已经尝试挑战过 \r\n#b赫卡顿#k 了。")
        sm.dispose()

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.HEKATON_TIME)
            sm.addCoolDownInXDaysForParty(destinations[response][4], 1, 7)
        else:
            sm.sendSayOkay("一个或多个队伍成员缺少前置任务，或等级低于 #b%d#k。" % destinations[response][1])
