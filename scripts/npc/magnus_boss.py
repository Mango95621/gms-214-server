from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type, Cooldown

destinations = [
    ["普通", 160, 401060200, 20, EventType.NMagnus, 64800000],
    ["困难", 220, 401060100, 20, EventType.HMagnus, 64800000],
]

runsPerDay = 1

if sm.getFieldID() == 401060000:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.setSpeakerID(3001032)

    dialog = "你想去 '#b暴君王座室#k' 挑战 \r\n#b麦格纳斯#k?\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往暴君王座室（%s 模式）#r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#不想去了"
    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("进入Boss需要进行组队。")
        sm.dispose()

    elif not sm.isPartyLeader():
        sm.sendSayOkay("如果你想进入，请让你的对账跟我谈谈 #b麦格纳斯#k.")
        sm.dispose()

    elif sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        timeUntilReset = sm.getTimeUntilEventReset(destinations[response][4])
        sm.sendNext("您或您的一名队员已经挑战过该副本 \r\n#b麦格纳斯#k 在过去18小时内.\r\n 还有 " + timeUntilReset + " 可以重新挑战此副本.")
        sm.dispose()

    elif not sm.hasItem(4033406):
        sm.sendSayOkay("你无法挑战该副本 #b#v 4033406 # #z 4033406 ##k.")
        sm.dispose()


    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setPartyDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(BossConstants.麦格纳斯_TIME)
            sm.addCooldownTimeForParty(destinations[response][4], destinations[response][5])
            sm.consumeItem(4033406)
        else:
            sm.sendSayOkay("一名或多名队员缺少进入副本的先决条件，或低于挑战级别 #b%d#k." % destinations[response][1])