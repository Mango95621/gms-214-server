from net.swordie.ms.constants import BossConstants
from net.swordie.ms.enums import EventType

# Mode, Required Level, Map ID, Death Count, Event Type, Cooldown

destinations = [
    ["简单", 50, 280030200, 5, EventType.EasyZakum, 21600000],
    ["普通", 75, 280030100, 5, EventType.NormalZakum, 21600000],
    ["困难", 120, 280030000, 5, EventType.ChaosZakum, 43200000],
]

runsPerDay = 1

if sm.getFieldID() == 211042400:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.setSpeakerID(2030008)

    dialog = "你想去 '#b扎昆的祭坛#k' 挑战#b扎昆吗#k?\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往扎昆的祭坛 (%s 难度) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#不想去了."
    response = sm.sendSay(dialog)

    if sm.getParty() is None:
        sm.sendSayOkay("请在进去之前创建一个队伍。")
        sm.dispose()

    elif not sm.isPartyLeader():
        sm.sendSayOkay("如果你想面对，请让你的队长跟我谈谈 #b扎昆#k.")
        sm.dispose()

    elif sm.partyHasCoolDown(destinations[response][4], runsPerDay):
        timeUntilReset = sm.getTimeUntilEventReset(destinations[response][4])
        sm.sendNext("您或您的一名队员最近已经挑战过 #b扎昆#k.\r\n\r\n 你有 #e#r" + timeUntilReset + "#n#k 分钟无法进行挑战.")
        sm.dispose()

    elif not sm.hasItem(4001017):
        sm.sendSayOkay("你不拥有 #b#v 4001017 # #z 4001017 ##k.")
        sm.dispose()


    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
          #  sm.addCooldownTimeForParty(destinations[response][4], destinations[response][5])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setPartyDeathCount(destinations[response][3])
            sm.setInstanceTime(BossConstants.ZAKUM_TIME)
        else:
            sm.sendSayOkay("一名或多名队员缺少进入副本的先决条件或低于挑战级别 #b%d#k." % destinations[response][1])