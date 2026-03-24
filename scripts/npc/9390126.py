from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type, Cooldown

destinations = [
    ["传奇", 240, 863010100, 20, EventType.Gollux, 172800000],
]

runsPerDay = 1

if sm.getFieldID() == 863010000:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.setSpeakerID(9390124)

    dialog = "你想前往'#b戈罗克斯之路#k'挑战 \r\n#b传奇戈罗克斯#k 吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往戈罗克斯之路 (%s 模式) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#算了。"
    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")
        sm.dispose()

    elif not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战 #b传奇戈罗克斯#k 的话。")
        sm.dispose()

    elif sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        timeUntilReset = sm.getTimeUntilEventReset(destinations[response][4])
        sm.sendNext("你或你的队伍成员在过去48小时内已经尝试挑战过 \r\n#b传奇戈罗克斯#k 了。\r\n 你的冷却时间还剩 " + timeUntilReset + "。")
        sm.dispose()

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.GOLLUX_TIME)
            sm.addCooldownTimeForParty(destinations[response][4], destinations[response][5])
        else:
            sm.sendSayOkay("一个或多个队伍成员缺少前置任务，或等级低于 #b%d#k。" % destinations[response][1])
