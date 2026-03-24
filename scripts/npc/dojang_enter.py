# So Gong (2091011) | Mu Lung Dojo Hall

dojoHall = 925020001

destinations = [
    ["简单", 70, 925070100],
    ["普通", 100, 925070200],
    ["困难", 130, 925070300],
    ["地狱", 160, 925070400],
    ["混沌", 160, 925070500],
    ["疯狂", 220, 925070600],

]

if sm.getFieldID() == dojoHall:
    selection = sm.sendNext("我的师父是武陵最强的人，而你想要挑战他？我感觉你会后悔的。\r\n#b"
                "#L0#我想挑战武陵道场。#l\r\n"
                "#L1#我想把我的点数分配给其他人。#l\r\n"
                "#L2#我想停止分配我的道场点数。#l\r\n"
                "#L3#我想看看谁在给我分配点数。#l\r\n")

    if selection == 0:
        if sm.getFieldID() == dojoHall:
            def is_party_eligible(reqlevel, party):
                for member in party.getMembers():
                    if member.getLevel() < reqlevel:
                        return False

                return True

            sm.sendSayOkay

            dialog = "请选择一个难度。\r\n"

            for i in range(len(destinations)):
                dialog += "#L%d##b%s 模式 (Lv. %d+)#l\r\n" % (i, destinations[i][0], destinations[i][1])

            dialog += "#L99#算了。"
            response = sm.sendSay(dialog)

            if sm.getParty() is None:
                sm.sendSayOkay("请先创建一个队伍再进去。")

            elif not sm.isPartyLeader():
                sm.sendSayOkay("请让你的队伍队长来和我对话，如果你想挑战武陵道场的话。")

            elif sm.checkParty() and response != 99:
                if is_party_eligible(destinations[response][1], sm.getParty()):
                    sm.warpInstanceIn(destinations[response][2], True)

                else:
                    sm.sendSayOkay("一个或多个队伍成员等级低于 %d。" % destinations[response][1])


    elif selection == 1:
        charName = sm.sendAskText("你想把道场点数分配给谁呢？", "", 4, 20)
        percentage = sm.sendAskNumber("你想把多少百分比的道场点数分配给他们？", 0, 1, 100)
        sm.addDojoLeader(charName, percentage)
        sm.sendNext("你现在正在分享 #r" + str(percentage) + "#b%#k 的点数给 #b" + str(charName) + "。\r\n#b")
    elif selection == 2:
        sm.removeDojoLeader()
        sm.sendNext("你不再分享你的点数了。\r\n#b")
    elif selection == 3:
        sm.sendNext(sm.getDojoContributorsList())
    elif selection == 4:
        sm.warpInstanceIn(706041650)
    elif selection == 99:
        sm.dispose()

elif not sm.hasMobsInField():
    chr.chatMessage("请等到怪物刷新后再离开地图。")
elif sm.hasMobsInField():
    sm.sendAskYesNo("你想离开吗？")
    sm.warpInstanceOutParty(925020001)
