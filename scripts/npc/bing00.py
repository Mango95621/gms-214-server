from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type

destinations = [
    ["普通", 235, 861000100, 5, EventType.AlienPQ],
]

runsADay = 5

if sm.getFieldID() == 861000000:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.sendAskYesNo

    dialog = "你想参加外星组队任务吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#b#L0#进入外星组队任务  -  " + str(sm.getEventAmountDone(EventType.getByVal(50))) + "/" + str(runsADay) + " 今天已尝试\r\n"

    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")
        sm.dispose()

    if not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想参加外星组队任务的话。")
        sm.dispose()

    if sm.partyHasCoolDown(destinations[response][4], runsADay):
        sm.sendNext("你或你的队伍成员在过去24小时内已经尝试过外星组队任务了。")
        sm.dispose()

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True, -384, -41)
            sm.setInstanceTime(5*60)
            sm.addCoolDownInXDaysForParty(destinations[response][4], 1, 1)
        else:
            sm.sendSayOkay("一个或多个队伍成员缺少前置任务，或等级低于 #b%d#k。" % destinations[response][1])
else:
    if sm.sendAskYesNo("你确定要离开战场吗？"):
        sm.warpInstanceOut(861000000)
