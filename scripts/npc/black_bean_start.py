from time import sleep

# Mode, Required Level, Map ID, Death Count

destinations = [
    ["简单", 10, 555001400, 5],
]

if sm.getFieldID() == 120040000:
    def is_party_eligible(reqlevel, party):
        for member in party.getMembers():
            if member.getLevel() < reqlevel:
                return False

        return True

    sm.sendAskYesNo

    dialog = "你想前往'#b阴凉海滩#k'挑战 \r\n#b黑豆#k 吗？\r\n"

    for i in range(len(destinations)):
        dialog += "#L%d##b前往阴凉海滩 (%s 模式) #r(Lv. %d+)#b#l\r\n" % (i, destinations[i][0], destinations[i][1])

    dialog += "#L99#算了。"
    response = sm.sendSay(dialog)

    if not sm.isPartyLeader():
        sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战 #b黑豆#k 的话。")

    if sm.getParty() is None:
        sm.sendSayOkay("请先创建一个队伍再进去。")

    elif sm.checkParty() and response != 99:
        if is_party_eligible(destinations[response][1], sm.getParty()):
            sm.setDeathCount(destinations[response][3])
            sm.warpInstanceIn(destinations[response][2], True)
            sm.setInstanceTime(20*60)
            sleep(1)
            sm.spawnMob(9420620, -500, 116, False, 200000000)
