# [Piston]  |  [9020009]
# Hidden Street : Stormfront

from net.swordie.ms.enums import EventType

mapId = 940021000
runsADay = 5

if sm.getFieldID() == 940020000:
    selection = sm.sendSayOkay("一些来自枫叶世界的坏蛋入侵了格兰蒂斯。我们需要找到方法把他们赶回去。\r\n"
                               "#L0##b进入维度入侵 " + str(sm.getEventAmountDone(EventType.DIPQ)) + "/" + str(runsADay) + " 今天已尝试 #l\r\n"
                               "#L1##b兑换维度手套碎片\r\n")

    if selection == 0:
        if chr.getLevel() < 120:
            sm.sendSayOkay("你必须达到 #b120#k 级才能进入维度入侵组队任务。")
            sm.dispose()

        if sm.getEventAmountDone(EventType.DIPQ) >= runsADay:
            sm.sendSayOkay("你目前正处于维度入侵组队任务的冷却时间。")
            sm.dispose()

        if not sm.getParty() is not None:
            sm.sendSayOkay("请先创建一个队伍再进入。")
            sm.dispose()

        if not sm.canHold(2431127):
            sm.sendSayOkay("请确保你的背包有足够的空间来接收组队任务结束时的奖励。")

        else:
            sm.addCoolDownInXays(EventType.DIPQ, 1, 1)
            sm.warpInstanceIn(mapId, True)
            sm.setInstanceTime(60*60)

    if selection == 1:
        selection2 = sm.sendSayOkay("请选择你想要的手套。\r\n"
                                    "#L0##b维度手套\r\n"
                                    "#L1##b高品质维度手套\r\n")

        if selection == 0:
            sm.sendAskYesNo("你想用你的 #b维度手套碎片#k 兑换一个 #b维度手套#k 吗？")

            if not sm.hasItem(4033605):
                sm.sendSayOkay("你没有 #v4033605##zv4033605#")
                sm.dispose()
            if not sm.hasItem(4033604):
                sm.sendSayOkay("你没有 #v4033604##zv4033604#")
                sm.dispose()
            if not sm.hasItem(4033603):
                sm.sendSayOkay("你没有 #v4033603##zv4033603#")
                sm.dispose()
            if not sm.hasItem(4033602):
                sm.sendSayOkay("你没有 #v4033602##zv4033602#")
                sm.dispose()
            if not sm.canHold(1082488):
                sm.sendSayOkay("请在装备背包里腾出空间。")
                sm.dispose()

            else:
                sm.consumeItem(4033605)
                sm.consumeItem(4033604)
                sm.consumeItem(4033603)
                sm.consumeItem(4033602)
                sm.giveItem(1082488)


        if selection == 1:
            sm.sendAskYesNo("你想用你的 #b高品质维度手套碎片#k 兑换一个 #b高品质维度手套#k 吗？")

            if not sm.hasItem(4033606):
                sm.sendSayOkay("你没有 #v4033606##zv4033606#")
                sm.dispose()
            if not sm.hasItem(4033607):
                sm.sendSayOkay("你没有 #v4033607##zv4033607#")
                sm.dispose()
            if not sm.hasItem(4033608):
                sm.sendSayOkay("你没有 #v4033608##zv4033608#")
                sm.dispose()
            if not sm.hasItem(4033609):
                sm.sendSayOkay("你没有 #v4033609##zv4033609#")
                sm.dispose()
            if not sm.canHold(1082488):
                sm.sendSayOkay("请在装备背包里腾出空间。")
                sm.dispose()

            else:
                sm.consumeItem(4033606)
                sm.consumeItem(4033607)
                sm.consumeItem(4033608)
                sm.consumeItem(4033609)
                sm.giveItem(1082489)
