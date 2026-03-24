from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type, Cooldown

destinations = [
    ["简单", 140, 272020200, 5, EventType.EArkarium, 64800000],
    ["普通", 170, 272020210, 5, EventType.Arkarium, 64800000],
]

runsPerDay = 1

if not 272020200 <= sm.getFieldID() <= 272020210:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    dialog = "你想前往'#b阿卡里乌姆的祭坛#k'挑战 \r\n#b阿卡里乌姆#k 吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往阿卡里乌姆的祭坛 (%s 模式) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#算了。"
    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")
        sm.dispose()

    elif not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战 #b阿卡里乌姆#k 的话。")
        sm.dispose()

    elif sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        timeUntilReset = sm.getTimeUntilEventReset(destinations[response][4])
        sm.sendNext("你或你的队伍成员在过去18小时内已经尝试挑战过 \r\n#b阿卡里乌姆#k 了。\r\n 你的冷却时间还剩 " + timeUntilReset + "。")
        sm.dispose()

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.ARKARIUM_TIME)
            sm.addCooldownTimeForParty(destinations[response][4], destinations[response][5])
        else:
            sm.sendSayOkay("一个或多个队伍成员缺少前置任务，或等级低于 #b%d#k。" % destinations[response][1])
else:
    if 272020200 <= sm.getFieldID() <= 272020210:
        if sm.sendAskYesNo("你确定要离开战场吗？"):
            sm.warpInstanceOutParty(272020110)
